from django.db import models
from resturant.models import Resturant
from food.models import Food

# Create your models here.
class Size(models.Model):
    sizee=models.CharField(max_length=60)
    price=models.FloatField()
    food_id=models.ForeignKey(Food,on_delete=models.CASCADE)

