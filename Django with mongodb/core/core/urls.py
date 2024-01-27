from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name='home'),
    
    path('receipes/', receipes, name='receipes'),
    
    path('delete-receipe/<int:id>', delete_receipe, name="delete_receipe"),
    path('update-receipe/<int:id>', update_receipe, name="update_receipe"),
    
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)
    

urlpatterns += staticfiles_urlpatterns() 
