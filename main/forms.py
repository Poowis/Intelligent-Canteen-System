from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(
        max_length=255, required=True, widget=forms.PasswordInput())


class RegisterForm(UserCreationForm):
    # TYPES = (
    #     ('user', 'user'),
    #     ('staff', 'staff')
    # )
    # user_type = forms.ChoiceField(choices=TYPES)

    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2",
                  "first_name", "last_name", "dob", "image_path"]


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


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["report_type", "detail"]


class OrderForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1)
    class Meta:
        model = Order
        fields = ['receive_datetime', "quantity", 'comment']


class AddMenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ['menu_name', 'description', 'prepare_time',
                  'image_path', 'price', 'amount', 'status']

class SearchForm(forms.Form):
    search = forms.CharField(required=False)
