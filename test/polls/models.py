import email
from django.db import models

# Create your models here.

class User(models.ModeL):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField()

class Booking(models.ModeL):
    date = models.DateField()
    start = models.CharField()
    end = models.CharField()
    name = models.ManyToManyField(User)