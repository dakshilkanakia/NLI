from django.db import models
from django.contrib.postgres.search import SearchVector
from django.db.models import Q 


# Create your models here.

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50,null = True)
    last_name = models.CharField(max_length=50,null = True)
    email = models.CharField(max_length=100,null = True)
    phone = models.CharField(max_length=100,null = True)
    affilation = models.CharField(max_length=100,null = True)
    position = models.CharField(max_length=100,null = True)
    city = models.CharField(max_length=100,null = True)
    state = models.CharField(max_length=100,null = True)
    zipcode = models.CharField(max_length=10,null = True)
    county = models.CharField(max_length=100,null = True)
    country = models.CharField(max_length=100,null = True)
    activity_type= models.CharField(max_length=100,null = True)
    activity_name = models.CharField(max_length=100,null = True)
    year = models.CharField(max_length=5,null = True)
    section = models.CharField(max_length=100,null = True)
    pass_fail = models.CharField(max_length=5,null = True)
    fee = models.CharField(max_length=100,null = True)
    sponsor = models.CharField(max_length=100,null = True)


    def __str__(self):
        return (f"{self.first_name} {self.last_name}")

