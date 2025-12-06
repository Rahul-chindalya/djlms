from django.urls import path
from . import views

app_name='one'

urlpatterns=[
    path('signup',views.signupuser.as_view(),name='signup'),
    path('userdata/<int:id>',views.userdata,name='userdata'),
]