from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(
        max_length=255, required=True, widget=forms.PasswordInput())


class RegisterForm(UserCreationForm):
    TYPES = (
        ('user', 'user'),
        ('staff', 'staff')
    )
    user_type = forms.ChoiceField(choices=TYPES)

    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2",
                  "first_name", "last_name", "dob", "image_path", "user_type"]


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ["res_id"]


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        exclude = ["rating", "users", "owner", "status"]


class AddStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ["user_id"]
