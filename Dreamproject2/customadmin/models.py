from django.db import models

# Create your models here.
class POST(models.Model):
    title = models.CharField(max_length=255)