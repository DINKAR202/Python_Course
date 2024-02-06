from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser
# from django.contrib.auth.models import 

# Create your models here.


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True , blank = True)
    
class CustomUser(AbstractUser):
    
    username = none
    email = models.EmailField("email_address", unique=True)
    
    USERNAME_FIELD = ['email']
    REQUIRED_FIELDS = []
    objects = CustomUser()
    
    def__str__(self):
        return self.email