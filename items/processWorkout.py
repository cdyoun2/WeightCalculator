import matplotlib.pyplot as plt
import numpy as np
import pandas
from .models import WorkoutEntry
import datetime


class ProcessWorkout():

    def process():
        deadlift = []
        bench = []
        squat = []
        clean = []
        snatch = []
        ohp = []
        dates = []
        deadlift = process_exercise('deadlift')
        bench = process_exercise('bench')
        squat = process_exercise('squat')
        clean = process_exercise('clean')
        snatch = process_exercise('snatch')
        ohp = process_exercise('ohp')

        for i in WorkoutEntry.objects.all():
            dates.append(i.date)

        # create the deadliftTonnage list
        deadliftTonnage = []
        benchTonnage = []
        squatTonnage = []
        cleanTonnage = []
        ohpTonnage = []
        snatchTonnage = []
        
        print('printing deadlift')
        print(deadlift)
        deadlift_tonnage_part = 0
        bench_tonnage_part = 0
        squat_tonnage_part = 0
        clean_tonnage_part = 0
        ohp_tonnage_part = 0
        snatch_tonnage_part = 0
        
        for i in deadlift:
            for j in i:
                deadlift_tonnage_part += j[0]*j[1]
            deadliftTonnage.append(deadlift_tonnage_part)
            deadlift_tonnage_part = 0
        for i in bench:
            for j in i:
                bench_tonnage_part += j[0]*j[1]
            benchTonnage.append(bench_tonnage_part)
            bench_tonnage_part = 0
        for i in squat:
            for j in i:
                squat_tonnage_part += j[0]*j[1]
            squatTonnage.append(squat_tonnage_part)
            squat_tonnage_part = 0
        for i in clean:
            for j in i:
                clean_tonnage_part += j[0]*j[1]
            cleanTonnage.append(clean_tonnage_part)
            clean_tonnage_part = 0
        for i in ohp:
            for j in i:
                ohp_tonnage_part += j[0]*j[1]
            ohpTonnage.append(ohp_tonnage_part)
            ohp_tonnage_part = 0
        for i in snatch:
            for j in i:
                snatch_tonnage_part += j[0]*j[1]
            snatchTonnage.append(snatch_tonnage_part)
            snatch_tonnage_part = 0

        print(deadliftTonnage)
        print(dates)

        # plot the values
       # plot the values
        plt.plot(dates, deadliftTonnage, color="orange",
                 marker="o", linestyle="dashed")
# add the bench line to the chart
        plt.plot(dates, benchTonnage, color="blue",
                 marker="o", linestyle="dashed")
        # add the squat line to the chart
        plt.plot(dates, squatTonnage, color="green",
                 marker="o", linestyle="dashed")
        # add the clean line to the chart
        plt.plot(dates, cleanTonnage, color="red",
                 marker="o", linestyle="dashed")
        # add the ohp line to the chart
        plt.plot(dates, ohpTonnage, color="purple",
                 marker="o", linestyle="dashed")
        # add the snatch line to the chart
        plt.plot(dates, snatchTonnage, color="black",
                    marker="o", linestyle="dashed")


        # set the x-axis to the dates
        plt.gcf().autofmt_xdate()

        # add labels for the x- and y-axes
        plt.xlabel("Date")
        plt.ylabel("Total Tonnage Lifted")
        # add a title to the chart
        plt.title("Total Tonnage Lifted Over Time")
        max_deadlift_tonnage = max(deadliftTonnage)
        plt.ylim(0, max_deadlift_tonnage+1000)
        # show the plot

        # show the plot
        plt.savefig('items/templates/items/plot.png')


def process_exercise(exercise):
    count = 0
    count_inner = 0
    exercise_set = []
    dates = []
    string_of_weight = ''
    string_of_reps = ''
    is_weight_flag = True
    exercise_array = []
    for i in WorkoutEntry.objects.all():
        print(i.__getattribute__(exercise))
        if (count == 0):
            for letter in i.__getattribute__(exercise):
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
                    print('testing inner reps, weight'+string_of_reps,
                          " | ", string_of_weight)
                    exercise_set.append([int(
                        string_of_weight), int(string_of_reps)])
                    string_of_weight = ''
                    string_of_reps = ''
                    count_inner += 1
                    count = count + 1
                print(letter)
            print('testing reps, weight'+string_of_reps,
                  " | ", string_of_weight)
            exercise_set.append(
                [int(string_of_weight), int(string_of_reps)])
            exercise_array.append(exercise_set)
            print(i.date)
            dates.append(i.date)
        count = 0
        is_weight_flag = True
        string_of_weight = ''
        string_of_reps = ''
        exercise_set = []
    return exercise_array
