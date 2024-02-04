from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.
def instructor_dashboard(request):
    context = {
        'title': 'Instructor dashboard',
    }
    return  render(request, "instructor-dashboard.html", context)