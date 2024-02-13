from djongo import models
from djongo.models import User
from django.conf import settings
from djongo.models import DjongoManager as CustomManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)