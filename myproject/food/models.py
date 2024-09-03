from django.db import models
from resturant.models import Resturant

# Create your models here.
class Food(models.Model):
    name=models.CharField(max_length=60)
    description=models.CharField(max_length=60)
    res_id=models.ForeignKey(Resturant,on_delete=models.CASCADE)
