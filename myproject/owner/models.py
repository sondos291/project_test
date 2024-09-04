from django.db import models

# Create your models here.
from users.models import CustomeUser
from resturant.models import Resturant
from adminn.models import Adminn

class Owner(CustomeUser):
    res_id=models.ForeignKey(Resturant,on_delete=models.CASCADE,null=True)
    adminn_fk=models.ForeignKey(Adminn,on_delete=models.CASCADE ,null=False, name="adminforignkey",default=1)
    # male=models.CheckConstraint()
