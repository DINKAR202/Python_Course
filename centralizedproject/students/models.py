from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True , blank = True)
    
class CustomUser(AbstractUser):
    
    username = none
    student_phone = models.CharField(max_length=100, unique=True)
    
    USERNAME_FIELD = ['student_phone']
    REQUIRED_FIELDS = []