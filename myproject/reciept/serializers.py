from rest_framework import serializers
from .models import Reciept


class RecieptSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Reciept
        fields="__all__"