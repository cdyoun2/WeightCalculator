from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import WorkoutEntry
from .forms import CreateWorkout
#from items.templates import WeightCalculator

# Create your views here.


def WorkoutEntries(request):
    # template_name = 'items/WeightCalculator.html'
    # model = WorkoutEntry
    # fields = ['deadlift', 'squat', 'bench', 'clean', 'snatch', 'ohp']

    # def displayWorkout(request):
    if request.method == 'POST':
        form = CreateWorkout(request.POST)
        if form.is_valid():
            deadlift = form.cleaned_data['deadlift']
            bench = form.cleaned_data['bench']
            squat = form.cleaned_data['squat']
            clean = form.cleaned_data['clean']
            snatch = form.cleaned_data['snatch']
            ohp = form.cleaned_data['ohp']
            example1 = WorkoutEntry()
            example1.bench = bench
            example1.squat = squat
            example1.deadlift = deadlift
            example1.clean = clean
            example1.snatch = snatch
            example1.ohp = ohp
            example1.save()
    form = CreateWorkout()
    return render(request, 'items/WeightCalculator.html', {"form": form})

    # def post(self, request, *args, **kwargs):
    #     WorkoutEntries.objects.create()
    #     WorkoutEntries.object.get(x=request.POST['form'])
    #     return HttpResponse("Success!")
