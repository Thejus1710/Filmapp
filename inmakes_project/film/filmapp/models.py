from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField()
    year=models.IntegerField()
    image=models.ImageField()

class More(models.Model):
    aname=models.CharField(max_length=50)
    aimage=models.ImageField()
    acname=models.CharField(max_length=50)
    acimage=models.ImageField(upload_to='static')