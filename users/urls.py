from django.urls import path
from . import views

app_name='one'

urlpatterns=[
    path('signup/',views.signupuser.as_view(),name='signup'),
    path('logout/',views.LogoutAPI.as_view(),name='logout'),
    path('login/',views.LoginAPI.as_view(),name='login'),
    path('userdata/<int:id>/',views.userdata,name='userdata'),
]