from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.

def Register(request):
    if(request.method=='POST'):                    
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        user.save()
        print('user created successfully')
        return redirect('/')
    else:
        return render(request,'Register.html')

def Login(request):
    return render(request,'Login.html')