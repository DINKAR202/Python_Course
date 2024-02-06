from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    context = {
        'title': 'Home page',
    }
    return  render(request, "index.html", context)

def login_page(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid username')
            return redirect('/login/')
        
        user = authenticate(request, username = username, password = password)
        
        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')
        
        else:
            login(request, user)
            # return redirect('/receipes/')
            return redirect('/student-dashboard/')
    
    context = {
        'title': 'Login Here',
    }
    return  render(request, 'sign-in.html', context)

def logout_page(request):
    logout(request)
    return redirect('/login/')


def sign_up(request):
    
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.filter(email = email)
        user_phone = User.objects.filter(phone=phone)
        
        if user.exists():
            messages.error(request, "Email already taken.")
            return redirect('/register/')
        
        elif user_phone.exists():
            messages.error(request, "Phone already taken.")
            return redirect('/register/')
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            user_phone = user_phone,
            email = email,
        )
        user.set_password(password)
        user.save()
        
        messages.info(request, "Account created Successfully")
        return redirect('/login/')
    
    context = {
        'title': 'Register Here',
    }
    return  render(request, 'sign-up.html', context)

@login_required(login_url="/login/")
def student_dashboard(request):
    context = {
        'title': 'Student Dashboard',
    }
    return  render(request, 'student-dashboard.html', context)





def forgot_password(request):
    context = {
        'title': 'forgot password here',
    }
    return  render(request, 'forgot-password.html', context)