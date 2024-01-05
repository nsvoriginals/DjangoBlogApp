

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Blog(models.Model):
    
    title = models.CharField(max_length=255)
    content = models.TextField() 