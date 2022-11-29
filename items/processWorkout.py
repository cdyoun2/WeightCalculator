from .models import WorkoutEntry


class ProcessWorkout():
    def process():
        for i in WorkoutEntry.objects.all():
            print(i.deadlift)
