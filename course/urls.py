from django.urls import path
from . import views

app_name="course"

urlpatterns=[
    path('courselist/',views.CourseList.as_view(),name="courselist"),
    path('coursedetail/<int:pk>/',views.CourseDetail.as_view(),name="coursedetail"),
]