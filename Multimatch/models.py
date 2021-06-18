from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

#install pip install django-phonenumber-field[phonenumbers]

# Create your models here.

class indexdata(models.Model):      #data model for the content in the index page
    heading=models.CharField(max_length=50)
    htext=models.TextField()
    himg=models.FileField(upload_to='indexpics') #destination where image of index page is stored
    h_main=models.BooleanField(default=False)
    h_left=models.BooleanField(default=False)
    h_right=models.BooleanField(default=False)


class purposedata(models.Model):        #data model for the content in th purpose page
    p_name=models.CharField(max_length=30)
    p_text=models.CharField(max_length=50)
    p_image=models.FileField(upload_to='indexpics')

class passionlist(models.Model):
    passion_name=models.CharField(max_length=50)


   
class Profile(models.Model):

    phone           =PhoneNumberField(null=False, blank=False, unique=True)               #new field
    date_of_birth   =models.DateField(null=True)   #newfield
    gender          =models.CharField(max_length=15)                    #new field
    height          =models.IntegerField(null=True)           #new fied 
    ethnicity       =models.CharField(max_length=50,null=True)      #new field
    nationality     =models.CharField(max_length=50,null=True)     #new field
    employment      =models.CharField(max_length=40,null=True)         #new field
    passionid1      =models.CharField(max_length=30)          #new field
    passionid2      =models.CharField(max_length=30)     
    passionid3      =models.CharField(max_length=30)     
    passionid4      =models.CharField(max_length=30)     
    passionid5      =models.CharField(max_length=30)     
    passionid6      =models.CharField(max_length=30)     
    passionid7      =models.CharField(max_length=30)     
    passionid8      =models.CharField(max_length=30)     
    passionid9      =models.CharField(max_length=30)     
    passionid10      =models.CharField(max_length=30)     
    purposeid       =models.CharField(max_length=30)          
    profilepic1      =models.FileField(upload_to='indexpics')
    profilepic2      =models.FileField(upload_to='indexpics')
    author          =models.OneToOneField('auth.User',unique=True,null=False, on_delete=models.CASCADE)

    def __unicode__(self):
            return self.title



    
    
    












