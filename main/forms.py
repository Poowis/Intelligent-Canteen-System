from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
    def clean_username(self):
        username = self.cleaned_data['username']
        return username

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2", "first_name", "last_name", "dob", "image_path"]