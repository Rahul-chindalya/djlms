from django.urls import path
from .views import LearnerProfileView

app_name = 'learner'

urlpatterns = [
    path('learnerprofile/', LearnerProfile.as_view(), name='learnerprofile'),
]