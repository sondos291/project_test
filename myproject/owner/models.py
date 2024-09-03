from django.db import models

# Create your models here.
from users.models import CustomeUser
from resturant.models import Resturant

class Owner(CustomeUser):
    res_id=models.ForeignKey(Resturant,on_delete=models.CASCADE)
