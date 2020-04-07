from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def Register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']

        # if(password==password1):
        #     if(User.objects.filter(email=email).exists()):
        #         messages.info(request,"Email is not used")
        #         return redirect('Register')
        #     elif(User.objects.filter(username=username).exists()):
        #         messages.info(request,"Username is not used")
        #         return redirect('Register')
        #     else:                
        #         user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        #         user.save()
        #         print('user created successfully')      
        # else:                
        #     messages.info(request,"Password is not match")
        #     return redirect('Register')                
        try:
            if(password!=password1):
                raise Exception("passwords are not matching....")
            if(User.objects.filter(email=email).exists()):
                raise Exception("Email is used....")
            elif(User.objects.filter(username=username).exists()):
                raise Exception("Username is used....")
            else:                
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                user.save()
                print('user created successfully')    
        except Exception as e:
            messages.info(request,str(e))
        finally:
            return redirect('Register')
            
    else:
        return render(request,'Register.html')

def Login(request):
    return render(request,'Login.html')