from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LearnerProfileSerializer
from .models import LearnerProfile
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.

# def is_admin(request):
#     return user.is_authenticated and getattr(user,'role',None)=='ADMIN'

class LearnerProfile(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request,pk):
        profile,_=  LearnerProfile.objects.get_object_or_create(user=request.data)
        serializer = LearnerProfileSerializer(profile)
        return Response(serializer.data)


    def put(self,request):
        profile = LearnerProfileSerializer.get_object_or_create(user=request.user)
        serializer =LearnerProfileSerializer(profile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


