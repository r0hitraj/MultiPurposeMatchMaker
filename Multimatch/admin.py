from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, indexdata, passionlist, purposedata

# Register your models here.
admin.site.register(indexdata) #here parameter is model class of indexdata table 

admin.site.register(purposedata) #here parameter is modal class of purpose table

admin.site.register(passionlist) #this is for passion list

admin.site.register(Profile) #this is for passion list

