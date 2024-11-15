from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class registerForm(forms.Form):
    txtClass = forms.TextInput(attrs={'class': 'form-control form-control-lg'})
    passwordClass = forms.PasswordInput(attrs={"class": "form-control form-control-lg"})

    login = forms.CharField(widget=txtClass, label="Login", max_length=50, required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg'}), label="Email", max_length=50, required=True)
    password = forms.CharField(widget=passwordClass, label="Hasło", max_length=50, required=True)
    password2 = forms.CharField(widget=passwordClass, label="Powtórz hasło", max_length=50, required=True)

class loginownform(forms.Form):
    loginClass = forms.TextInput(attrs={"class": "form-control form-control-lg"})
    passwordClass = forms.PasswordInput(attrs={"class": "form-control form-control-lg"})

    login = forms.CharField(widget=loginClass, label="Login", max_length=50, required=True)
    password = forms.CharField(widget=passwordClass, label="Password", max_length=50, required=True)

class createEntryForm(forms.Form):
    txtClass = forms.TextInput(attrs={'class': 'form-control form-control-lg'})

    content = forms.CharField(widget=txtClass, label="Content", max_length=500, required=True)
