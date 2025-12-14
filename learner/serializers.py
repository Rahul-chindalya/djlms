from rest_framework import serializers
from .models import LearnerProfile
from django.contrib.auth import get_user_model
from course.serializers import CourseSerializer
from batch.serializers import BatchSerializer
from course.models import Course        
from batch.models import Batch  

User = get_user_model()

class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','role']

class LearnerProfileSerializer(serializers.ModelSerializer):
    user =SimpleUserSerializer(read_only=True)
    enrolled_courses = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), many=True, required=False)
    enrolled_batches = serializers.PrimaryKeyRelatedField(queryset=Batch.objects.all(), many=True, required=False)

    class Meta:
        model = LearnerProfile
        fields = ['id','user','phone','dob','bio','enrolled_courses','enrolled_batches','created_at']
        read_only_fields = ['created_at']