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
                        # reset the weight and reps strings
                        string_of_weight = ''
                        string_of_reps = ''
                        count_inner += 1
                    print(letter)
                count = count + 1
                print('testing reps, weight'+string_of_reps,
                      " | ", string_of_weight)
                deadlift.append([
                    int(string_of_weight), int(string_of_reps)])
            count = 0
            is_weight_flag = True
            string_of_weight = ''
            string_of_reps = ''

        print(i.date)
        dates.append(i.date)

        # create the deadliftTonnage list
        deadliftTonnage = []
        for i in deadlift:
            deadliftTonnage.append(i[0]*i[1])

        deadliftTonnage.append(1500)
        dates.append(datetime.date(2020, 1, 1))
        dates.append(datetime.date(2020, 1, 2))

        print(deadliftTonnage)
        print(dates)

        # plot the values
        plt.plot(dates, deadliftTonnage)

        # set the x-axis to the dates
        plt.gcf().autofmt_xdate()

        # show the plot
        plt.savefig('items/templates/items/plot.png')
