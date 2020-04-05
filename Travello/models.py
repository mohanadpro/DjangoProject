from django.db import models

# Create your models here.

# make the class as a model to be migrated to the database
class Destination(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    img=models.ImageField(upload_to='pics')
    price=models.IntegerField()
    offer=models.BooleanField(default=False)