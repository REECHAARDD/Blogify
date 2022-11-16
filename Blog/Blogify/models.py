from datetime import datetime
from tkinter import CASCADE
from django.db import models
from distutils.command.upload import upload
from email.policy import EmailPolicy, default
from django.contrib.auth.models import User
from django.urls import reverse

class SignUp(models.Model):
    firstName = models.CharField(max_length=30,null=False)
    LastName = models.CharField(max_length=30,null=False)
    username = models.CharField(max_length=10,null=False)
    Email = models.EmailField(EmailPolicy,max_length=50,null=False)
    password = models.CharField(max_length=10,null=False)
    confirmpassword = models.CharField(max_length=10,null=False)

class signin(models.Model):
    username = models.CharField(max_length=10,null=False)
    password = models.BooleanField(null=False)

class Preview(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    image =  models.ImageField( upload_to="Posts", height_field=None, width_field=None, max_length=None,null=True)
    content = models.TextField(max_length=100)
    
class post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="Posts", null=True)
    Written_at  = models.DateTimeField("Date published",default=datetime.now,blank=False)
    image =  models.ImageField( upload_to="Posts", height_field=None, width_field=None, max_length=None,null=True )
    content = models.TextField(max_length=120)
    Author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' ' + str(self.Author)
    
    def get_absolute_url(self):
        return reverse("Home.html")

 
