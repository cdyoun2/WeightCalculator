from django import forms


class CreateWorkout(forms.Form):
    deadlift = forms.CharField(label="deadlift", max_length=200)
    squat = forms.CharField(label='squat', max_length=200)
    bench = forms.CharField(label='bench', max_length=200)
    clean = forms.CharField(label='clean', max_length=200)
    snatch = forms.CharField(label='snatch', max_length=200)
    ohp = forms.CharField(label='ohp', max_length=200)
