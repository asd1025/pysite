from django.shortcuts import render

# Create your views here.

def index(requeset):
    return render(requeset,'main/index.html')