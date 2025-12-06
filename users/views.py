from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.

@method_decorator(csrf_exempt,name='dispatch')
class signupuser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

def userdata(request):
    user = User.objects.get(id=1)
    serializer = UserSerializer(user)
    jsonData = JSONRenderer().render(serializer.data)
    return HttpResponse(jsonData,content_type='application/json')