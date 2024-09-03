from django.db import models
from subprice.models import SubPrice
from users.models import CustomeUser

# Create your models here.
class Reciept(models.Model):
    subprice_fk=models.ForeignKey(SubPrice,on_delete=models.CASCADE)
    user_fk=models.ForeignKey(CustomeUser,on_delete=models.CASCADE)
    totalPrice=models.DecimalField(decimal_places=2,max_digits=6)
    