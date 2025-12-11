from django.contrib import admin
from .models import Batch

# Register your models here.
@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display=['id','name','course']