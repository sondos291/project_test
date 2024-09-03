from rest_framework import serializers
from .models import Food
from resturant.models import Resturant

class foodserializer(serializers.ModelSerializer):
    
    class Meta:
        model=Food
        fields="__all__"