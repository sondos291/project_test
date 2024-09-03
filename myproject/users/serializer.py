from rest_framework import serializers
from .models import CustomeUser
from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.views import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomeUser
        fields = '__all__'

    def create(self, validated_data):
        user = CustomeUser(
            username=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data['phone']
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user
    
class TokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()    






































# from rest_framework import serializers
# from users.models import CustomeUser
# # from rest_framework_simplejwt.views import TokenObtainPairSerializer



# from rest_framework import serializers
# from django.contrib.auth.models import User
# from rest_framework_simplejwt.tokens import RefreshToken
# from .models import CustomeUser

# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = CustomeUser
#         fields = ('username', 'password', 'email')

#     def create(self, validated_data):
#         user = CustomeUser.objects.create_user(**validated_data)
#         return user

# class TokenSerializer(serializers.Serializer):
#     refresh = serializers.CharField()
#     access = serializers.CharField()







    
            

       

