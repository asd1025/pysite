from django.db.models import Max
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from board.models import Board
from user.models import User


def list(request):
    board = Board.objects.all().order_by('-regdate')
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
    print(board)
    return render(request,'board/view.html',data)

def modify(request,id=0):
    board=Board.objects.filter(id=id)
    data={'board':board[0]}
    return render(request,'board/modify.html',data)

def update(request,id=0):
    board=Board()
    board.content =
    return HttpResponseRedirect(f'board/view/{id}')