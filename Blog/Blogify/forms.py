from dataclasses import fields
from email.message import EmailMessage
from email.mime import image
from email.policy import EmailPolicy
from enum import unique
from pyexpat import model
from tkinter import Widget
from turtle import title
from typing_extensions import Required
from django import forms
from .models import *
from django.forms import fields, widgets
from .models import SignUp,signin,post


class Signupform(forms.ModelForm):
    firstname = forms.CharField(label='firstname',max_length=30,required=True,help_text='Optional')
    lastname = forms.CharField(label='lastname',max_length=30, required=True,help_text='Optional')
    username = forms.EmailField(label='username',max_length=30)
    Email = forms.EmailField(label='Email',max_length=100,help_text='Valid Email address required')
    password = forms.CharField(max_length=10,null=False)
    confirmpassword = forms.CharField(max_length=10,null=False)

class Signinform(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=100,unique=True)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)



class Postform (forms.ModelForm):
    class Meta:
        model = post
        fields = ('title','tag','content','author','image','tags')

        widgets ={
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'tag' : forms.TextInput(attrs={'class':'form-control'}),
            'author' : forms.TextInput(attrs={'class':'form-control','value':''} ),
            'content' : forms.TextInput(attrs={'class':'form-control'})
        }




class Editform (forms.ModelForm):
    class Meta:
        model = post
        fields = ('title','tag','content')

        widgets ={
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'tag' : forms.TextInput(attrs={'class':'form-control'}),
            'body' : forms.TextInput(attrs={'class':'form-control'})
        }

