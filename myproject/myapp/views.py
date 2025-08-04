from django.shortcuts import render
from myproject.celery import add
from .task import sub
from celery.result import AsyncResult

# Create your views here.
def index(request):
    print("Result:")
    result = add.delay(10,20)
    print(result)
    
    return render(request,"home.html",{'result':result})


def about(request,id):
    print("Result:")
    result = AsyncResult(id)
    result.get()
    return render(request,"about.html",{'result':result})


def contact(request):
    print("Result:")
    return render(request,"contact.html")