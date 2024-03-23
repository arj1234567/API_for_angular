from rest_framework import serializers
from .models import Userdata_tb

class UserSerializer(serializers.ModelSerializer):
    Full_name = serializers.CharField(max_length=20)
    Email = serializers.CharField(max_length =20)
    Password = serializers.CharField(max_length=20)
    
    class Meta:
        model=Userdata_tb
        fields = '__all__'