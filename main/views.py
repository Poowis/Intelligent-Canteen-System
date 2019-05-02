from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    context = {
        "items": [0, 1, 2]
    }
    return render(request, "main/index.html", context=context)


def logIn(request):
    context = {
        "asd": "asd"
    }
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        print(request.user.user_type)
    return render(request, "main/login.html", context=context)