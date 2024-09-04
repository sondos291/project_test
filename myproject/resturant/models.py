from django.db import models
from adminn.models import Adminn

# Create your models here.
class Resturant(models.Model):
    name=models.CharField(max_length=60)
    phone=models.IntegerField()
    Address=models.CharField(max_length=60)
    img=models.ImageField( blank=True, null=True)
    admin_fk=models.ForeignKey(Adminn,on_delete=models.CASCADE,default=1)
