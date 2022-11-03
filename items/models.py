from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Item(models.Model):
    text = models.CharField(max_length=2000)


class WorkoutEntry(models.Model):
    deadlift = []
    squat = []
    bench = []
    clean = []
    snatch = []
    ohp = []
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
