from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import OwnerCreateView

urlpatterns = [
    path('createowner/', OwnerCreateView.as_view(), name='user-signup'),
    
    
    ]
   