from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import NewUserForm, LogForm
from django.contrib import messages 
import bcrypt
from django.contrib.auth import authenticate, login 
from django.contrib.auth.hashers import make_password

def index(request):
    context={
        "form" : NewUserForm(),
        "logform" : LogForm()

    }
    return render(request, 'index.html',context)

def add_user(request):
    if request.method=='POST':
        bound_form=NewUserForm(request.POST)
        if len(bound_form.errors) > 0:
            for key, value in bound_form.errors.items():
               messages.error(request,value)
            return redirect('/')
        User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=make_password(request.POST['password1']),
            username=request.POST['username']
        )
        user=User.objects.get(id=id)
        return redirect('/success')

def user_login(request):
    if request.method =='POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user != None:
            login(request,user)

            return redirect ('/success')
       
    messages.error(request, "Incorrect Login")
    return redirect ('/')



def success(request):
    messages.success(request, "You have logged in successfully!")
    return render(request, 'success.html')

def logout(request):
    request.session.clear()
    return redirect('/')