from django import forms


class CreateWorkout(forms.Form):
    deadlift = forms.CharField(label="deadlift", max_length=200)
    squat = forms.CharField(label='squat', max_length=200)
    bench = forms.CharField(label='bench', max_length=200)
    clean = forms.CharField(label='clean', max_length=200)
    snatch = forms.CharField(label='snatch', max_length=200)
    ohp = forms.CharField(label='ohp', max_length=200)


class LoginForm(forms.Form):
    username_to_login = forms.CharField(label='username', max_length=200)
    password = forms.CharField(label='password', max_length=200)


class RegisterForm(forms.Form):
    username_to_register = forms.CharField(label='username', max_length=200)
    password = forms.CharField(label='password', max_length=200)
