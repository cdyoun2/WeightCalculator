from django.shortcuts import render
from django.views import generic
from items.models import Item
from django.http import HttpResponse
from .models import WorkoutEntry
#from items.templates import WeightCalculator

# Create your views here.


class ItemList(generic.ListView):
    template_name = 'items/WeightCalculator.html'
    context_object_name = 'item_list'
    model = Item

    def post(self, request, *args, **kwargs):
        Item.objects.create(text=request.POST["text"])
        return HttpResponse("Success!")


class WorkoutEntries (generic.ListView):
    template_name = 'items/WeightCalculator.html'
    model = WorkoutEntry
    fields = ['deadlift', 'squat', 'bench', 'clean', 'snatch', 'ohp']

    def displayWorkout(request):
        return render(request, 'WeightCalculator.html')

    def post(self, request, *args, **kwargs):
        WorkoutEntries.objects.create(text=request.POST["text"])
        return HttpResponse("Success!")
