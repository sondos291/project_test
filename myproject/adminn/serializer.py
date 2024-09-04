from rest_framework import serializers
from adminn.models import Adminn

class adminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Adminn
        fields = '__all__'

    def create(self, validated_data):
        user = Adminn(
            name=validated_data['name'],
            is_admin=validated_data['is_admin'],
            phone=validated_data['phone'],
            
        )
        # user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user
    
class TokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField() 
