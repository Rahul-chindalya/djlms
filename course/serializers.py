from rest_framework import serializers
from .models import Course
#You will break the project if you later change to a custom user model.(if u directliy import from models)
from django.contrib.auth import get_user_model
#Then User will always point to whatever User model your project is using — default or custom. 

User = get_user_model()

class TrainerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields =['id','username','email']

class CourseSerializer(serializers.ModelSerializer):
    trainer = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='TRAINER'),many=True)

    trainer_details = TrainerInfoSerializer(source='trainer',many=True,read_only=True)

    class Meta:
        model =Course
        fields = ['id','title','desc','dur_weeks','trainer','trainer_details','created_at']
        read_only_fields =['created_at']