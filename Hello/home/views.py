from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    context = {
        "variable":"this is my variable",
        "variable1":"chalo thik h"
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('this is about page')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email=email, phone=phone, desc=desc, date = datetime.today())
        
    return render(request, 'contact.html')
