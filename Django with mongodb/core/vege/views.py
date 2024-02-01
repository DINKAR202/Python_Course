from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.shortcuts import render, redirect


# Create your views here.

@login_required(login_url="/login/")
def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        
        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image,
        )
        
        return redirect('/receipes/')
    
    queryset = Receipe.objects.all()
    
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))
    
    context = {'receipes': queryset}   
    return render(request, 'receipes.html', context)

@login_required(login_url="/login/")
def update_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    context = {'receipe': queryset}   
    
    return render(request, 'update_receipes.html', context)
    


def delete_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    # print("ID", queryset)
    queryset.delete()
    return redirect('/receipes/')
    
    
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not get_user_model().objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect(reverse('login'))
        
        user = authenticate(request, username=username, password=password)
        
        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect(reverse('login'))
        
        else:
            login(request, user)
            next_url = request.GET.get('next', reverse('receipe'))  # Redirect to 'receipe/' or the URL specified in 'next'
            return redirect(next_url)
            
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect(reverse('login'))


def register(request):
    
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        
        user = User.objects.filter(username = username)
        
        if user.exists():
            messages.error(request, "Username already taken.")
            return redirect('/register/')
    
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email,
        )
        user.set_password(password)
        user.save()
        
        messages.info(request, "Account created Successfully")
        return redirect('/login/')
    
    return render(request, 'register.html')