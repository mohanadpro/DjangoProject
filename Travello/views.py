from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):
    dest=Destination()
    dest.name='Dubai'
    dest.description='Khalifa tower'
    dest.price=200
    dest.img='destination_1.jpg'


    dest1=Destination()
    dest1.name='Lus Anjlus'
    dest1.description='City that is not sleep'
    dest1.price=400
    dest1.img='destination_2.jpg'

    dest2=Destination()
    dest2.name='Paris'
    dest2.description='Tour Eiffel'
    dest2.price=300
    dest2.img='destination_3.jpg'
    
    dests=[dest,dest1,dest2]
    return render(request,'index.html',{'dests':dests})