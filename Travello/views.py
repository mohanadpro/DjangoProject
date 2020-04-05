from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):
    dest=Destination()
    dest.name='Dubai'
    dest.description='City that is not sleep'
    dest.price=200
    
    return render(request,'index.html',{'dest':dest})