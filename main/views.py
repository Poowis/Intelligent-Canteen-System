from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import *

# Create your views here.

def index(request):
    context = {
        "items": [0, 1, 2]
    }
    return render(request, "main/index.html", context=context)


def my_login(request):
    context = {
        "asd": "asd"
    }
    if request.method == "POST":
        form = LoginForm(request.POST)
        form.is_valid()
        print(form.cleaned_data)
        user = authenticate(request, username=form.cleaned_data["username"], password=form.cleaned_data["password"])
        if user:
            login(request, user)
            return redirect('index')
        else:
            context["form"] = form
    else:
        context["form"] = LoginForm()
    return render(request, "main/login.html", context=context)


def my_logout(request):
    context = {}
    logout(request)
    return render(request, "main/login.html", context=context)

def my_register(request):
    context = {
        "asd": "asd"
    }
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data["password1"])
            user = authenticate(request, username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
            login(request, user)
            return redirect('index')
        else:
            return redirect('register')
    else:
        context["form"] = RegisterForm()
    return render(request, "main/register.html", context=context)
    