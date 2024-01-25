from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hey there i'm django")

def about(request):
    return HttpResponse("<h1>Hey there this is about page</h1>")