from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from .managers import CustomManager

# Create your models here.

class CustomUser(AbstractUser):
        
        username = None
        email = models.EmailField("email_address", unique=True)        
        USERNAME_FIELD = "email"
        REQUIRED_FIELDS = []
        objects = CustomManager()
        
        def __str__(self):
            return self.email


class Student(models.Model):
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True , blank = True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    # email = models.EmailField(unique=True)
    # phone = models.CharField(max_length=15)
    