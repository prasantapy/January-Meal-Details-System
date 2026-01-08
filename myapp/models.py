from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=40)
    advance = models.CharField(max_length=40,null= True)
    location = models.TextField(null = True)
    date = models.DateField(null=True, blank=True)
    lunch = models.CharField(max_length=10,null = True)
    dinner = models.CharField(max_length=10,null= True)
    extra_meals = models.TextField(null= True)
    
