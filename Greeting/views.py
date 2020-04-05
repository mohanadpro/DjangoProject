from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'Home.html',{'name':'Mohanad'});


def add(request):
    number1=int(request.POST['num1'])
    number2=int(request.POST['num2'])
    res=number1+number2

    return render(request,'res.html',{'res':res})
