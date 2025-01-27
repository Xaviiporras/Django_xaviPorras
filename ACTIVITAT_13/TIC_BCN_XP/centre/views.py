from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def proff(request):
    prof = {"name": "Roger", "surname": "Sobrino", "age": "23"}
    return render(request, 'proff.html', {'nom': prof["name"], 'cognom': prof["surname"], 'edat': prof["age"]})

def users(request):
    alum = {"name": "Oriol", "surname": "Roca", "age": "18"}
    return render(request, 'users.html', {'alumn': alum})

# Create your views here.
