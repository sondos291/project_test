from django.shortcuts import render
from rest_framework import generics ,permissions,status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from .models import Food
from .serializer import foodserializer
from rest_framework.views import APIView

# Create your views here.
from rest_framework import viewsets

class foodviewset(viewsets.ModelViewSet):
    queryset=Food.objects.all()
    serializer_class=foodserializer

    # def post(self,request):
    #     serializer=foodserializer(data=request.data)
    #     if  serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


