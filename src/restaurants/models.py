from django.db import models
from django.utils import timezone

# Create your models here.

class restaurantLocations(models.Model):
    name        = models.CharField(max_length=120)
    location    = models.CharField(max_length=120,null=True,blank=True)
    category    = models.CharField(max_length=120,null=True,blank=True)
    created     = models.DateTimeField(auto_now_add=True,blank=True)
    modified    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


