from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import UserSignUpView, UserLoginView

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='user-signup'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]