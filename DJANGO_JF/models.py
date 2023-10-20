from django.db import models
from django.contrib.auth.models import AbstractUser

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)