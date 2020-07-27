from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "hello/index.html")

def rishi(request):
    return HttpResponse("Hello Rishi!")

def greet(request, name):
    return render(request, "hello/greet.html",{
        #render function take optional third argument which is called the context
        "name" : name.capitalize()
    })