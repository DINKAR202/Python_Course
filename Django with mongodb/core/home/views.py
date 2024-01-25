from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    peoples = [
        {'name':'Abhishek Gupta', 'age':'26'},
        {'name':'Ragni', 'age':'21'},
        {'name':'Neha kamti', 'age':'27'},
        {'name':'Dinkar Raj', 'age':'16'},
        {'name':'Preety singh', 'age':'22'}
    ]
    
    vegetables = ['Pumpkin', 'Tomato', 'Potatoe']    
    
    return render(request, "home/index.html", context={'peoples':peoples, 'vegetables':vegetables})
    

def about(request):
    return render(request, "home/about.html")
    