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
        # username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not Students.objects.filter(email = email).exists():
            messages.error(request, 'Invalid email')
            return redirect('/login/')
        
        user = authenticate(request, email = email, password = password)
        
        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')
        
        else:
            login(request, user)
            return redirect('/student-dashboard/')
    
    context = {
        'title': 'Login here',
    }
    return  render(request, 'sign-in.html', context)

def logout_page(request):
    logout(request)
    return redirect('/login/')


def sign_up(request):
    
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # username = request.POST.get('username')
        date_of_birth = request.POST.get('date_of_birth')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = Students.objects.filter(email = email)
        # user_username = Students.objects.filter(username=username)
        
        if user.exists():
            messages.error(request, "Email already taken.")
            return redirect('/register/')
        
        # elif user_username.exists():
        #     messages.error(request, "Username already taken.")
        #     return redirect('/register/')
        
        user = Students.objects.create(
            first_name = first_name,
            last_name = last_name,
            date_of_birth = date_of_birth,
            phone_number = phone_number,
            address = address,
            # username = username,
            email = email,
        )
        user.set_password(password)
        user.save()
        
        messages.info(request, "Account created Successfully")
        return redirect('/login/')
    
    context = {
        'title': 'Register here',
    }
    return  render(request, 'sign-up.html', context)

@login_required(login_url="/login/")
def student_dashboard(request):
    context = {
        'title': 'Student dashboard',
    }
    return  render(request, 'student-dashboard.html', context)





def forgot_password(request):
    context = {
        'title': 'forgot password here',
    }
    return  render(request, 'forgot-password.html', context)