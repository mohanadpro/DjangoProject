from django.contrib import admin

from .models import Destination
# Register your models here.


# in this way we can register our model to be able to more destination
admin.site.register(Destination)