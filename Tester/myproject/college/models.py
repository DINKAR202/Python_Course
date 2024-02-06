from django.db import models

# Create your models here.
class College(models.Model):
    CollegeName = models.CharField(max_length=100, unique=True)
    CollegeCode = models.CharField(max_length=50, unique=True)
    adminAdministrator = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.CollegeName