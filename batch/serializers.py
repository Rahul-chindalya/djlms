from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Batch
from course.models import Course

User = get_user_model()

class TrainerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']

class LearnerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']

class CourseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','title']

class BatchSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    trainer =  serializers.PrimaryKeyRelatedField(
        queryset = User.objects.filter(role='TRAINER'),
        allow_null= True,
        required= False
    )
    learner = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.filter(role='LEARNER'),
        many = True,
        required = False
    )
    course_details = CourseInfoSerializer(source='course',read_only=True)
    trainer_details = TrainerInfoSerializer(source='trainer',read_only=True)
    learner_details = LearnerInfoSerializer(source = 'learner',read_only=True,many=True)
     
    class Meta:
        model = Batch
        fields = ['id','name','course','course_details','trainer','trainer_details','learner','learner_details','start_date','end_date']