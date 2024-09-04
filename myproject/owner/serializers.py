from rest_framework import serializers

from owner.models import Owner
from django.contrib.auth.hashers import make_password

class Ownerserializer(serializers.ModelSerializer):
    
    class Meta:
        model=Owner
        fields="__all__"

    def update(self, instance,validated_date):
        instance.password=validated_date.get('password',instance.password)
        instance.save()
        return instance























    # def validate(self, data):
    #     if data['new_password'] != data['confirm_password']:
    #         raise serializers.ValidationError("Passwords do not match.")
    #     return data

    # def update_password(self, owner, validated_data):
    #     owner.password = make_password(validated_data['new_password'])
    #     owner.save()
    #     return owner   
    

        
    