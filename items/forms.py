from django import forms


class CreateWorkout(forms.Form):
    deadlift = forms.CharField(label="Deadlift", max_length=200,
                               widget=forms.TextInput(attrs={'placeholder': 'Enter your Deadlift'}))
    squat = forms.CharField(label='Squat', max_length=200,
                            widget=forms.TextInput(attrs={'placeholder': 'Enter your Squat'}))
    bench = forms.CharField(label='Bench Press', max_length=200,
                            widget=forms.TextInput(attrs={'placeholder': 'Enter your Bench Press'}))
    clean = forms.CharField(label='Clean', max_length=200,
                            widget=forms.TextInput(attrs={'placeholder': 'Enter your Clean'}))
    snatch = forms.CharField(label='Snatch', max_length=200,
                             widget=forms.TextInput(attrs={'placeholder': 'Enter your Snatch'}))
    ohp = forms.CharField(label='Overhead Press', max_length=200,
                          widget=forms.TextInput(attrs={'placeholder': 'Enter your Overhead Press'}))
