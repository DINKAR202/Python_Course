from django.contrib import admin
from .models import *
# Register your models here.

# @admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')  # Add 'phone' to the list display
    # search_fields = ['email', 'First Name', 'Last Name']  # Add 'phone' to the search fields
admin.site.register(CustomUser)
admin.site.register(Student)
