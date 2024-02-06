from django.contrib import admin
from .models import *
# Register your models here.

# @admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email')  # Add 'phone' to the list display
    search_fields = ['email']  # Add 'phone' to the search fields
admin.site.register(CustomUser)
