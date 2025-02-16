from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from login.models import Usuario
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate


def index(request):
    return render(request, 'index.html')

def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Usuario.objects.get(email=email)
            if password == user.password:
                return redirect('home')
            else:
                messages.error(request, 'Credenciales inválidas')
        except Usuario.DoesNotExist:
            messages.error(request, 'Usuario no encontrado')
    
    return render(request, 'login.html')