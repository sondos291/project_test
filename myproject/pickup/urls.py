from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import PickUpViewSet

router=DefaultRouter()
router.register(r'pickup',PickUpViewSet)

urlpatterns=[
    path('',include(router.urls))
]