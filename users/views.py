from django.shortcuts import render
from .models import User
from .serializers import UserSerializer,loginSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from django.contrib.auth import login,logout
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication


# Create your views here.

@method_decorator(csrf_exempt,name='dispatch')
class signupuser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

def userdata(request,id):
    user = User.objects.get(id=id)
    serializer = UserSerializer(user)
    jsonData = JSONRenderer().render(serializer.data)
    return HttpResponse(jsonData,content_type='application/json')

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        # Override and do nothing instead of raising an exception
        return
class LogoutAPI(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        logout(request)
        return Response(
            {"msg":"logout Successfull"},
            status=status.HTTP_200_OK
        )

@method_decorator(csrf_exempt,name='dispatch')
class LoginAPI(APIView):
    authentication_classes=[]
    permission_classes = [AllowAny]

    def post(self ,request):
        serializer = loginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request,user)
            return Response({
                'msg':"LOGIN Successfull",
                'role':user.role
            },status=status.HTTP_200_OK)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)