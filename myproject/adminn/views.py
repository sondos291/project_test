from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Adminn
from .serializer import AdminSerializer

class AdminnViewSet(viewsets.ModelViewSet):
    queryset = Adminn.objects.all()
    serializer_class = AdminSerializer
