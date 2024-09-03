from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import OwnerViewSet

router=DefaultRouter()
router.register(r'owner',OwnerViewSet)

urlpatterns=[
    path('',include(router.urls))
]