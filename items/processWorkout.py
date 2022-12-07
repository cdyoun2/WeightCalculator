import matplotlib.pyplot as plt
import numpy as np
import pandas
from .models import WorkoutEntry
import datetime


class ProcessWorkout():
    def parse_the_cursed_string():
        pass

    def process():
        count = 0
        count_inner = 0
        deadlift = []
        bench = []
        squat = []
        clean = []
        snatch = []
        ohp = []
        dates = []
        string_of_weight = ''
        string_of_reps = ''
        is_weight_flag = True
        for i in WorkoutEntry.objects.all():
            if (count == 0):
                for letter in i.deadlift:
                    if letter == 'x':
                        is_weight_flag = False
                    if letter == ',':
                        is_weight_flag = True
                    if is_weight_flag and letter != 'x' and letter != ',':
                        string_of_weight += letter
                    if (not is_weight_flag and letter != 'x' and letter != ','):
                        string_of_reps += letter
                    if letter == ',':
                        print('testing reps, weight'+string_of_reps,
                              " | ", string_of_weight)
                        deadlift.append([
                            int(string_of_weight), int(string_of_reps)])
                        string_of_weight = ''
                        string_of_reps = ''
                        count_inner += 1
                    print(letter)
                count = count + 1
                deadlift.append([
                    int(string_of_weight), int(string_of_reps)])
        for i in WorkoutEntry.objects.all():
            if (count == 0):
                for letter in i.bench:
                    if letter == 'x':
                        is_weight_flag = False
                    if letter == ',':
                        is_weight_flag = True
                    if is_weight_flag and letter != 'x' and letter != ',':
                        string_of_weight += letter
                    if (not is_weight_flag and letter != 'x' and letter != ','):
                        string_of_reps += letter
                    if letter == ',':
                        print('testing reps, weight'+string_of_reps,
                              " | ", string_of_weight)
                        bench.append([
                            int(string_of_weight), int(string_of_reps)])
                        string_of_weight = ''
                        string_of_reps = ''
                        count_inner += 1
                    print(letter)
                count = count + 1
                bench.append([
                    int(string_of_weight), int(string_of_reps)])
        dates.append(i.date)

        dates2 = []
        for i in range(30):
            dates2.append(datetime.date.today() - datetime.timedelta(days=i))

        # create a list of values
        values = np.random.randint(0, 100, 30)

        # plot the values
        plt.plot(dates, deadlift)

        # set the x-axis to the dates
        plt.gcf().autofmt_xdate()

        # show the plot
        plt.savefig('items/templates/items/plot.png')
