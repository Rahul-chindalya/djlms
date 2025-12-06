from rest_framework import serializers
from .models import Course
from django.contrib>auth import get_user_model

User = get_user_model()

class TrainerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields =['id','username','email']

class CourseSerializer(serializers.ModelSerializer):
    triners = serializers.PrimeKeyRelatedField(queryset=User.objects.filter(role='TRAINER'),many=True)

    trainer_details = TrainerInfoSerializer(source='trainer',many=True,read_only=True)

    class Meta:
        model =Course
        fields = ['id','title','desc','dur_weeks','trainer','trainer_details','created_at']