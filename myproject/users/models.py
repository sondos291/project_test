from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomeUser(AbstractBaseUser):
    
    username=models.CharField(max_length=60,unique=True)
    email=models.EmailField(max_length=50,unique=True)
    password=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)

    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
   
