from dataclasses import fields
from email.message import EmailMessage
from email.policy import EmailPolicy
from enum import unique
from pyexpat import model
from typing_extensions import Required
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


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



