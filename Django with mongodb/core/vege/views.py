# from django.shortcuts import render, redirect
# from .models import *
# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
# # Create your views here.

# def receipes(request):
#     if request.method == "POST":
#         data = request.POST
#         receipe_name = data.get('receipe_name')
#         receipe_description = data.get('receipe_description')
#         receipe_image = request.FILES.get('receipe_image')
        
#         Receipe.objects.create(
#             receipe_name = receipe_name,
#             receipe_description = receipe_description,
#             receipe_image = receipe_image,
#         )
        
#         return redirect('/receipes/')
    
#     queryset = Receipe.objects.all()
#     context = {'receipes': queryset}   
#     return render(request, 'receipes.html', context)

# def update_receipe(request, id):
#     queryset = Receipe.objects.get(id = id)
#     context = {'receipe': queryset}   
    
#     return render(request, 'update_receipes.html', context)
    


# def delete_receipe(request, id):
#     queryset = Receipe.objects.get(id = id)
#     print("ID", queryset)
#     queryset.delete()
#     return redirect('/receipes/')
    
    
from django.shortcuts import render, redirect, get_object_or_404
from .models import Receipe

def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        
        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image,
        )
        
        return redirect('/receipes/')
    
    queryset = Receipe.objects.all()
    context = {'receipes': queryset}   
    return render(request, 'receipes.html', context)

def update_receipe(request, id):
    receipe = get_object_or_404(Receipe, id=id)
    context = {'receipe': receipe}   
    return render(request, 'update_receipes.html', context)

def delete_receipe(request, id):
    if id is not None:
        id = int(id)
        receipe = get_object_or_404(Receipe, id=id)
        receipe.delete()
        return redirect('/receipes/')
    else:
        # Handle the case where 'id' is None (or redirect to an error page)
        return HttpResponse("Invalid request")
