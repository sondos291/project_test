from rest_framework import serializers
from .models import SubPrice


class SubPriceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=SubPrice
        fields="__all__"