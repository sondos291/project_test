
from django.db import models

class Adminn (models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    is_admin=models.BooleanField(default=False)
    password=models.CharField(max_length=60,null=False ,default="",blank=True)
