from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        "items": [0, 1, 2]
    }
    return render(request, "main/index.html", context=context)