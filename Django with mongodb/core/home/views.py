from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    peoples = [
        {'name':'Abhishek Gupta', 'age':'26'},
        {'name':'Ragni', 'age':'21'},
        {'name':'Neha kamti', 'age':'27'},
        {'name':'Dinkar Raj', 'age':'19'},
        {'name':'Preety singh', 'age':'22'}
    ]
    return render(request, "home/index.html", context={'peoples':peoples})
    

def about(request):
    return HttpResponse("<h1>Hey there this is about page</h1>")