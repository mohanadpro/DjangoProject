from django.db import models

# Create your models here.

class Destination:
    id:int
    name:str
    description:str
    img:str
    price:float
    offer:bool