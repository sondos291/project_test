from django.db import models

# Create your models here.
class Resturant(models.Model):
    name=models.CharField(max_length=60)
    phone=models.IntegerField()
    Address=models.CharField(max_length=60)
    img=models.ImageField( blank=True, null=True)
