from django.shortcuts import render
from django.utils import timezone

# Create your views here.
def say_hello(request,name):
    
    return render(request,'say_hello.html',{'name':name})

def Time(request):
    now = timezone.now()
    return render(request,'say_hello.html',{'now':now})