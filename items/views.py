from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import *
from .forms import *
# from items.templates import WeightCalculator
from .processWorkout import ProcessWorkout
import datetime
import matplotlib.pyplot as plt
from django.contrib.auth import authenticate, login
# import user
from django.contrib.auth.models import User
# import redirect
from django.shortcuts import redirect


# Create your views here.


def WorkoutEntries(request):
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
            example1.date = datetime.date.today()
            example1.user = request.user
            print('savingf entry')
            example1.save()
    form = CreateWorkout()
    return render(request, 'items/WeightCalculator.html', {"form": form})


class WorkoutList(generic.ListView):
    template_name = 'items/viewWorkout.html'
    context_object_name = 'workout_list'
    model = WorkoutEntry

    def get_queryset(self):
        ProcessWorkout.process(self.request.user)
        print(self.request.user)
        return WorkoutEntry.objects.filter(user=self.request.user)


def plot_view(request):
    image_data = open("items/templates/items/" +
                      request.user.__str__() + "plot.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")


def home_view(request):
    login_form = LoginForm(request.POST)
    register_user_form = RegisterForm(request.POST)
    if 'username_to_login' in request.POST:
        if login_form.is_valid():
            username_to_login = login_form.cleaned_data['username_to_login']
            password = login_form.cleaned_data['password']
            User2 = User.objects.get(username=username_to_login)
            print('we are here')
            if (type(User2) is not str):
                if (User2.check_password(password)):
                    print('login successful')
                    login(request, User2)
                    return redirect('workout')
    if 'username_to_register' in request.POST:
        if register_user_form.is_valid():
            username_to_register = register_user_form.cleaned_data['username_to_register']
            password = register_user_form.cleaned_data['password']
            User2 = User.objects.create_user(
                username_to_register, '', password)

    context = {'login_form': login_form,
               'register_user_form': register_user_form}
    return render(request, 'items/home.html', context=context)
