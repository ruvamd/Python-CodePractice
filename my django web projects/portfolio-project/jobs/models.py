from django.db import models
from django.contrib import Job
from .models import Job
# Create your models here.
admin.site.register(Job)

class Job(models.Model):
    image=models.ImageField(upload_to='images/')
    summary=models.CharField(max_length=200)