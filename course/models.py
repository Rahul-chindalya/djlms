from django.db import models
from django.conf import settings
# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    dur_weeks = models.PositiveBigIntegerField(default=4)
    trainer = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        limit_choices_to={'role':"TRAINER"},
        related_name = 'TRAINER',
    )
    createdd_at = models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title 