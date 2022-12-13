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


class LoginForm(forms.Form):
    username_to_login = forms.CharField(label='username', max_length=200)
    password = forms.CharField(label='password', max_length=200)


class RegisterForm(forms.Form):
    username_to_register = forms.CharField(label='username', max_length=200)
    password = forms.CharField(label='password', max_length=200)
