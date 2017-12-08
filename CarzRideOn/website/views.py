from django.shortcuts import render


def login(request):
    return render(request, 'website/login.html', {"temp": "temp"})


def index(request):
    return render(request, 'website/index.html', {"temp": "temp"})


def signup(request):
    return render(request, 'website/login.html', {"temp": "temp"})
