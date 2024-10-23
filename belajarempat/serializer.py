from rest_framework import serializers
from .models import UserBelajarEmpat

class UserBelajarEmpatSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBelajarEmpat
        fields = '__all__' 