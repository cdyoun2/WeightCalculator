from .models import WorkoutEntry


class ProcessWorkout():
    def process():
        count = 0
        count_inner = 0
        deadlift = []
        string_of_weight = ''
        string_of_reps = ''
        is_weight_flag = True
        for i in WorkoutEntry.objects.all():
            if (count == 0):
                # print(i.deadlift)
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

        print(deadlift)
