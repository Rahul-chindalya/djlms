from django.db import models
from django.conf import settings
from course.models import Course
from batch.models import Batch

# Create your models here.

class LearnerProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name='learner_profile'
    )
    phone = models.CharField(max_length=20 , blank = True  ,null = True)
    dob = models.DateField(blank = True  ,null = True)
    enrolled_courses = models.ManyToManyField(Course,blank = True  ,null = True,related_name='learner')
    bio = models.TextField(blank = True  ,null = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - learner profile"
        