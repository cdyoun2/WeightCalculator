from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class WorkoutEntry(models.Model):
    deadlift = models.CharField(max_length=300, default=" ")
    squat = models.CharField(max_length=300, default=" ")
    bench = models.CharField(max_length=300, default=" ")
    clean = models.CharField(max_length=300, default=" ")
    snatch = models.CharField(max_length=300, default=" ")
    ohp = models.CharField(max_length=300, default=" ")
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #date = models.DateTimeField(auto_now_add=True)
