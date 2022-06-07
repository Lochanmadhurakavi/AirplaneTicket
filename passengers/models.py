from distutils.command.upload import upload
from pyexpat import model
from tokenize import blank_re
from django.db import models

# Create your models here.

class Passenger(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    choice = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = models.CharField(max_length=1, choices=choice, null=True)
    country = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name
        
         
