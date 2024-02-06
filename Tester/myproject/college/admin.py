from django.contrib import admin
from college.models import *
# Register your models here.

class CollegeAdmin(admin.ModelAdmin):
    list_display=['CollegeName', 'CollegeCode', 'adminAdministrator', 'phone', 'email']
admin.site.register(College,CollegeAdmin)