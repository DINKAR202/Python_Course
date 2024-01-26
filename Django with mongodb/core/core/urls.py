from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *

urlpatterns = [
    path('', home, name='home'),
    
    path('receipes/', receipes, name='receipes'),
    
    path('delete-receipe/<id>/', delete_receipe, name="delete_receipe"),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    
    path('admin/', admin.site.urls),
]

