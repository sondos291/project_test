from rest_framework import serializers

from owner.models import Owner

class Ownerserializer(serializers.ModelSerializer):
    
    class Meta:
        model=Owner
        fields="__all__"