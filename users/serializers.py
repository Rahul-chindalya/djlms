from rest_framework import serializers
# from django.contrib.auth import get_user_model
from .models import User
from django.contrib.auth import authenticate
 
#create your serialezers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields =['username','email','password','role']

    def create(self,validate_data):
        user = User.objects.create_user(**validated_data)
        return user
##  its converts plain password in ##hash code to secure data
    def create(self,validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
######################################################

class loginSerializer(serializers.Serializer):
    username =  serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self,data):
        user = authenticate(
            username=data['username'],
            password=data['password']
        )
        if not user:
            raise serializers.ValidationError("Invalid Credentials")
        data['user']=user
        return data