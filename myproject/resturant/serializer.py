from rest_framework import serializers
from .models import Resturant


class resturantserializer(serializers.ModelSerializer):
    
    class Meta:
        model=Resturant
        fields="__all__"