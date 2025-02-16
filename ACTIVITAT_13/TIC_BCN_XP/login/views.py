from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from login.models import Usuario

def index(request):
    return render(request, 'index.html')

def home_view(request):
    if 'user_id' in request.session:
        user_id = request.session.get('user_id')
        user = Usuario.objects.get(id=user_id)
        return render(request, 'home.html', {'user': user})
    else:
        return redirect('login')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Usuario.objects.get(email=email)
            if password == user.password:
                request.session['user_id'] = user.id 
                return redirect('home') 
            else:
                messages.error(request, 'Credenciales inválidas')
        except Usuario.DoesNotExist:
            messages.error(request, 'Usuario no encontrado')

    return render(request, 'login.html')

def logout_view(request):
    request.session.flush()
    return redirect('login')
