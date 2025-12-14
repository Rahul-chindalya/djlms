from django.urls import path
from .views import LearnerProfile

app_name = 'learner'

urlpatterns = [
    path('learnerprofile/', LearnerProfile.as_view(), name='learnerprofile'),
]