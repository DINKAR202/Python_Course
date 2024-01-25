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
    
    text="Lorem ipsum, dolor sit amet consectetur adipisicing elit. Animi vero veritatis qui beatae quidem aspernatur atque a deserunt eligendi ullam quos cumque corporis voluptatum voluptate incidunt eaque commodi, accusamus maxime ipsa voluptatem soluta natupudiandae perferendis odit. Facilis ipsum perferendis consectetur, odio repellendus veniam? Error ab labore ut optio aliquid sequi earum, doloribus accusantium dolores animi obcaecati qui id ipsum dignissimos sunt ipsam? Nisi rem cum voluptas!"
    return render(request, "home/index.html", context={'peoples':peoples, 'text':text})
    

def about(request):
    return HttpResponse("<h1>Hey there this is about page</h1>")