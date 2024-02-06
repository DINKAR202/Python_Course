from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class Student(models.Model):
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True , blank = True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)