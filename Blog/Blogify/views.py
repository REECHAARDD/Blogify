from django.shortcuts import render
import email
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import  User,auth
from django.forms import PasswordInput
from .models import post, signin
from django.views.generic import ListView,CreateView,DetailView
from django.forms import *
from .models import SignUp

def index(request):
    return render(request,'index.html')

def Signup(request):
    if request.method == 'POST':
        Firstname = request.POST['Firstname']
        Lastname = request.POST['Lastname']
        username = request.POST['username']
        email = request.POST['email']
        Password = request.POST['Password']
        ConfirmPassword = request.POST['ConfirmPassword']

        if Password == ConfirmPassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=Password)
                user.save();
                messages.success(request,'<h3>You are now registered </h3>')
                return redirect('Signin')
        else:
            messages.info(request, 'Password Not Matching!!')
            return redirect('signup')
    else:
        return render(request, 'signUp.html')

def Signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate (username=username,password=password)

        if user is not None :
            auth.login(request,user)
            return redirect('Home')
        else :
            messages.info(request,'Username or Password is wrong! ')
            return redirect ('Signin')
    else :
        return render (request,'Signin.html')

def logout(request):
    auth.logout(request)
    return redirect ('')
 
def preview(request):
    posts = post.objects.all()
    return render(request,'preview.html',{'posts':posts})

def post(request,pk):
    posts = post.objects.get(id=pk)
    return render(request,'post.html',{'posts':posts})

class Createblog(CreateView):
    model = post
    template_name = "Createblog.html"
    fields = "__all__"
    

# class Blog (ListView):
#     model = post
#     template_name ="Homepage.html"
#     context_object_name = 'posts'

def Blog (request):
    return render(request,'Homepage.html')

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

