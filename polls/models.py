import email
from unicodedata import name
from django.db import models

# Create your models here.

class Contact(models.Model):
    Firstname = models.CharField(max_length=122)
    Lastname = models.CharField(max_length=122)
    Email = models.CharField(max_length=155)
    Password = models.CharField(max_length=155)
    Address = models.CharField(max_length=155)
    Address2 = models.CharField(max_length=155)
    City = models.CharField(max_length=155)
    State = models.CharField(max_length=155)
    Date = models.DateField()

    def __str__(self): 
        return self.Firstname

