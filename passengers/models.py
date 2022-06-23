from django.db import models
from cloudinary.models import CloudinaryField

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
    image = CloudinaryField("image", overwrite=True, resource_type="image", 
                            transformation={"quality": "auto:eco"},
                            format="jpg",)

    def __str__(self):
        return self.name
        
         
