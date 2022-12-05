from django.db import models

# Create your models here.
class Part(models.Model):
    Part_ID = models.IntegerField(primary_key=True)
    Part = models.CharField(max_length=50) 
    Cat = models.IntegerField()

class Cat(models.Model):
    Catnumb = models.IntegerField(primary_key=True)
    Cat_name = models.CharField(max_length=50) 
    Price = models.FloatField()
