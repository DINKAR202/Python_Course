from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
class Postcategory(models.Model):
    cat_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    