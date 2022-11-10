from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50)
    