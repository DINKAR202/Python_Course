from django.db import models
from django.contrib.auth.models. import User



class Receipe(models.Model):
    receipe_name = models.CharField(max_length=150)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to="receipe")