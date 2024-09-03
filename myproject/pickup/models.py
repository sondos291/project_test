from django.db import models
from users.models import CustomeUser
from owner.models import Owner

# Create your models here.
class PickUp(models.Model):
    user_fk=models.ForeignKey(CustomeUser,on_delete=models.CASCADE,related_name='pickupsusername')
    owner_fk=models.ForeignKey(Owner,on_delete=models.CASCADE, related_name='pickupsowner')
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('ready', 'Ready'),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    time=models.TimeField()