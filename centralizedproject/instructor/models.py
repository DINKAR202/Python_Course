from django.db import models

# Create your models here.
class Instructor(models.Model):
    full_name = models.CharField(max_length=30)
    
    email = models.EmailField(max_length=254)