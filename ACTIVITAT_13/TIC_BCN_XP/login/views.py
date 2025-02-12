from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request, 'index.html')

def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')
