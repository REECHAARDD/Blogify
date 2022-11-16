from django.shortcuts import render
import email
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import  auth
from django.forms import PasswordInput
from .models import post
from django.views.generic import ListView,CreateView,DetailView

def index(request):
    return render(request,'index.html')

def Signup(request):
    if request.method == 'POST':
        Firstname = request.POST['Firstnamee']
        Lastname = request.POST['Lastname']
        username = request.POST['username']
        Email = request.POST['Email']
        Password = request.POST['Password']
        ConfirmPassword = request.POST['Confirm Password']

        if Password == ConfirmPassword:
            if user.object.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect(request,'Signup.html')
            elif user.objects.filter(Username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect(request,'Signup.html')
            else:
                user = user.object.create_user(username=username,EmailL=Email,PASSWORD=Password)
                user.save();
                return redirect(request,'Signin.html')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('Signup.html')
    else:
        return render(request, 'Signup.html')


def Signin(request):
    if request.method == 'POST':
        Username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate (Username=Username,password=password)
        if user is not None :
            auth.login(request,user)
            return redirect('Homepage.html')
        else :
            messages.info(request,'credential invalid ')
            return redirect ('Signin.html')
    else :
        return render (request,'signin.html')


def preview(request):
    posts = post.objects.all()
    return render(request,'preview.html',{'posts':posts})

def post(request,pk):
    posts = post.objects.get(id=pk)
    return render(request,'post.html',{'posts':posts})

def logout(request):
    auth.logout(request)
    return redirect (request,'index.html')


class Createblog(CreateView):
    model = post
    template_name = "Createblog.html"
    fields = "__all__"
    

class Blog (ListView):
    model = post
    template_name ="Homepage.html"
    context_object_name = 'posts'


class Articledetailview(DetailView):
    model = post
    template = "Article_detail.html"


def editpage(request):
    return render (request,'edit.html')

def Contactus(request):
    return  render(request, 'Contactus.html') 

def about(request):
    return render(request, 'About.html')

def Politics(request):
    return render(request, 'Politics.html')

def sports(request):
    return render(request, 'sports.html')

def Entertainment(request):
    return render(request, 'Entertainment.html')
    
def fashion(request):
    return render(request, 'fashion.html')
    
def politics(request):
    return render(request, 'politics.html')
    
def business(request):
    return render(request, 'business.html')

def music(request):
    return render(request, 'music.html')
