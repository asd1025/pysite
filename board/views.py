from django.db.models import Max, F
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from board.models import Board
from user.models import User


def list(request):
    board = Board.objects.all().order_by('-groupno','orderno')
    for g in board:
        print(g)
    data = {'boardlist': board}
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

def view(request,id=0):
    board=Board.objects.filter(id=id)
    data={'board':board[0]}
    return render(request,'board/view.html',data)

def modify(request,id=0):
    board=Board.objects.filter(id=id)
    data={'board':board[0]}
    return render(request,'board/modify.html',data)

def update(request,id=0):
    board = Board.objects.get(id=id)
    board.content = request.POST['content']
    board.title = request.POST['title']
    board.save()
    return HttpResponseRedirect(f'/board/view/{id}')

def reply(request,id=0):
    # groupno = 1 이고 orderno >= 2 의 게시물의
    # orderno를 1씩 증가
    # __gt, __lt, __gte, __lte
    board = Board.objects.get(id=id)
    # orderno update 후 insert
    Board.objects.filter(groupno=board.id).filter(orderno__gte=board.orderno+1).update(orderno=F('orderno') + 1)
    board.save()

    reply=Board()
    reply.title = request.POST['title']
    reply.content = request.POST['content']
    reply.user = User.objects.get(id=request.session['authuser']['id'])
    reply.groupno = board.groupno
    reply.orderno = board.orderno+1
    reply.depth = board.depth+1
    reply.save()
    return HttpResponseRedirect(f'/board/')


