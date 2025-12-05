from django.db import models
from django.conf import settings
from course.models import Course
# Create your models here.

class Batch(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='batches')
    trainer = models.ForeignKey(
        settings.AUTH_USER_MODEL ,
        on_delete= models.SET_NULL,
        null = True,
        limit_choices_to ={'role':'TRAINER'},
        related_name='batches',
    )
    learner = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        limit_choices_to ={'role':'LEARNER'},
        related_name='learner',
        )
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.course.title})"