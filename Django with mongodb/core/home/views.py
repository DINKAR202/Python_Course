from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(rewuest):
    return HttpResponse("Hey there i'm django")