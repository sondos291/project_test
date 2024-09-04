from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics ,permissions,status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from .models import Resturant
from .serializer import resturantserializer
from rest_framework.views import APIView
from .permissions import IsAdminUser


# Create your views here.
from rest_framework import viewsets

class resturantviewset(viewsets.ModelViewSet):
    queryset=Resturant.objects.all()
    serializer_class=resturantserializer
    permission_classes = [ IsAdminUser]

    def perform_create(self, serializer):
        # Optionally, you can add extra logic here
        serializer.save()











    # def post(self,request):
    #     serializer=resturantserializer(data=request.data)
    #     if  serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

