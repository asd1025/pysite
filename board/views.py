

from django.db.models import Max, F, Q
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from board.models import Board
from board.paging import Paging
from user.models import User

def getTotalCount():
    count=Board.objects.all().count()
    return count


def search(request):
    kwd = request.POST.get('kwd','')
    return list(request,kwd)

def list(request,kwd=''):

    prevGroupNo = int(request.GET.get('prevGroupNo',0))
    pageNo = int(request.GET.get('pageNo',1))
    kwd=request.GET.get('kwd',kwd)
    if kwd != '':
        board = Board.objects.filter(Q(title__contains=kwd)|Q(content__contains=kwd)).filter(delete=False)
        paging = Paging(allCount=len(board))
        paging.getPaging(prevGroupNo, pageNo)
        board = board.order_by('-groupno','orderno')[paging.startPageNo:paging.startPageNo+paging.contentsCount]
    else :
        paging = Paging(allCount=getTotalCount())
        paging.getPaging(prevGroupNo, pageNo)
        board = Board.objects.all().order_by('-groupno', 'orderno')[paging.startPageNo:paging.startPageNo + paging.contentsCount]
    data = {'boardlist': board, "paging":paging, 'page_list': range(paging.startPageGroupNo+1,paging.startPageGroupNo+paging.groupCount+1),'kwd':kwd }

    return render(request, 'board/list.html', data)

def writeform(request):
    id = request.session.get('authuser','')
    if id == '':
        return HttpResponseRedirect('/user/loginform?result=require')
    return render(request, 'board/write.html')

def write(request):
    board = Board()
    board.title=request.POST['title']
    board.content=request.POST['content']
    board.user= User.objects.get(id=request.session['authuser']['id'])
    board.groupno=counter_max()
    board.save()
    return HttpResponseRedirect('/board')


def counter_max():
    value=Board.objects.aggregate(max_groupno=Max('groupno'))
    max_groupno=0 if value['max_groupno'] is None else value['max_groupno']
    return max_groupno+1

def hit_check(visits='',id=0):
    board = Board.objects.get(id=id)

    if id in visits and visits != '':
        data={'board':board, 'hitable':False}
        return data

    board.hit = board.hit + 1
    board.save()
    data = {'board': board, 'hitable': True}
    return data

def view(request,id=0):
    board=Board.objects.get(id=id)
    if request.COOKIES.get('visits') is None:
        data=hit_check(id=str(id))
        response = render(request, 'board/view.html',data)
        response.set_cookie('visits', str(id), max_age=60*60)
        #visits = request.COOKIES.get('visits')
        return response

    else:
        visits = request.COOKIES.get('visits')
        data=hit_check(visits,str(id))
        response = render(request, 'board/view.html', data)
        if  data['hitable'] :
            visits= visits +' | ' + str(id)
        response.set_cookie('visits',visits,max_age=60*60)
        return response

def modify(request,id=0):
    board=Board.objects.filter(id=id)
    data={'board':board[0]}
    return render(request,'board/modify.html',data)

def update(request,id=0):
    user_id = request.session.get('authuser', '')
    if user_id == '':
        return HttpResponseRedirect('/user/loginform?result=require')
    board = Board.objects.get(id=id)
    board.content = request.POST['content']
    board.title = request.POST['title']
    board.save()
    return HttpResponseRedirect(f'/board/view/{id}')

def reply(request,id=0):
    # __gt, __lt, __gte, __lte /// groupno = 1 이고 orderno >= 2 의 게시물의 orderno를 1씩 증가
    user_id = request.session.get('authuser', '')
    if user_id == '':
        return HttpResponseRedirect('/user/loginform?result=require')
    board = Board.objects.get(id=id)
    # orderno update 후 insert
    Board.objects.filter(groupno=board.groupno).filter(orderno__gte=board.orderno+1).update(orderno=F('orderno') + 1)

    reply=Board()
    reply.title = request.POST['title']
    reply.content = request.POST['content']
    reply.user = User.objects.get(id=request.session['authuser']['id'])
    reply.groupno = board.groupno
    reply.orderno = board.orderno+1
    reply.depth = board.depth+1
    reply.save()
    return HttpResponseRedirect(f'/board/')


def delete(request,id=0):
    user_id = request.session.get('authuser', '')
    if user_id == '':
        return HttpResponseRedirect('/user/loginform?result=require')
    board=Board.objects.filter(id=id).update(delete=True)
    return HttpResponseRedirect(f'/board/')



