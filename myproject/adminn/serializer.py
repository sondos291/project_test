from rest_framework import serializers
from adminn.models import Adminn
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Adminn
        fields=['id','name','phone','is_admin']