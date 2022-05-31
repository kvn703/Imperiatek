import email
from django.db import models
import mysql.connector

# Create your models here.

class User(models.ModeL):
    u_name = models.CharField(max_length=50)
    u_surname = models.CharField(max_length=50)
    u_email = models.EmailField()
    u_password = models.CharField()

class Booking(models.ModeL):
    date = models.DateField()
    start = models.DateField()
    end = models.DateField()
    name = models.CharField()
