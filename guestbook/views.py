from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from guestbook.models import Guestbook


def list(request):
    guestbook=Guestbook.objects.all().order_by('-regdate')
    for g in guestbook:
        print(g)
    data={'guestbook':guestbook}
    return render(request,'guestbook/list.html',data)

def deleteform(request,id=0):
    data={'no':id}
    return render(request,'guestbook/deleteform.html',data)

def delete(request,id=0):
    guestbook = Guestbook()
    id = request.POST['no']
    guestbook.password = request.POST['password']
    guestbook=Guestbook.objects.filter(id=id,password=guestbook.password)
    # DB 에 넣어서 저장하겠다
    guestbook.delete()

    # insert 후 꼭 redirect
    return HttpResponseRedirect('/guestbook')


def insert(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['pass']
    guestbook.content = request.POST['content']

    # DB 에 넣어서 저장하겠다
    guestbook.save()

    # insert 후 꼭 redirect
    return HttpResponseRedirect('/guestbook')