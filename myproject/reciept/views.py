from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics ,permissions,status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from .models import Reciept
from reciept.serializers import RecieptSerializer

# Create your views here.
from rest_framework import viewsets

class RecieptViewSet(viewsets.ModelViewSet):
    queryset=Reciept.objects.all()
    serializer_class=RecieptSerializer
