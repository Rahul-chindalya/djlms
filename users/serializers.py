from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User  
 
#create your serialezers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields =['username','email','password','role']

    def create(self,validate_data):
        user = User.objects.create_user(**validate_data)
        return user