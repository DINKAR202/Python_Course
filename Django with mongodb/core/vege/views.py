from django.shortcuts import render

# Create your views here.
def receipes(request):
    data = request.POST
    print(data)
    return render(request, 'receipes.html')