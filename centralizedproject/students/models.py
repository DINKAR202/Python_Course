from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True , blank = True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"