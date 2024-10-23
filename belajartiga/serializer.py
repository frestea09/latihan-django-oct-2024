from rest_framework import serializers
from .models import UserBelajarTiga

class UserBelajarTigaSerializer(serializers.ModelSerializer):
   class Meta:
      model = UserBelajarTiga
      fields ='__all__'