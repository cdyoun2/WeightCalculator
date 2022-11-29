from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import WorkoutEntry
from .forms import CreateWorkout
#from items.templates import WeightCalculator
from .processWorkout import ProcessWorkout

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

# class ViewWorkout
# def ViewWorkout(request):
#     context_object_name = 'workout_list'
#     workout1 = ProcessWorkout()
#     ProcessWorkout.process()
#     return render(request, 'items/viewWorkout.html')


class WorkoutList(generic.ListView):
    template_name = 'items/viewWorkout.html'
    context_object_name = 'workout_list'
    model = WorkoutEntry
    ProcessWorkout.process()

    def get_queryset(self):
        return WorkoutEntry.objects.filter()
