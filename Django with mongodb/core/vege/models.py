from django.db import models
from django.contrib.auth.models import User



class Receipe(models.Model):
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null = True , blank = True)
    receipe_name = models.CharField(max_length=150)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to="receipe")
    
class User(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=60)