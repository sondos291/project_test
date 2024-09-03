from django.db import models
from food.models import Food
from size.models import Size

# Create your models here.
class SubPrice(models.Model):
    food_fk=models.ForeignKey(Food, on_delete=models.CASCADE)
    size_fk=models.ForeignKey(Size,on_delete=models.CASCADE)
    quantity =models.IntegerField()
    totalsupprice=models.DecimalField(decimal_places=2,max_digits=6)


