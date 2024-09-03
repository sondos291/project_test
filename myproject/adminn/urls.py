from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import AdminnViewSet

router=DefaultRouter()
router.register(r'admin',AdminnViewSet)

urlpatterns=[
    path('',include(router.urls))
]