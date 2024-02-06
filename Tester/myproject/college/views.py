from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def college_register(request):
    
    context = {
        'title': 'College Registration',
    }
    return render(request, 'college-register.html', context)

def college_login(request):
    
    context = {
        'title': 'College Login',
    }
    return render(request, 'college-login.html', context)