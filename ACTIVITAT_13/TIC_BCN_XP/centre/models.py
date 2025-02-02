from django.db import models

class Persona(models.Model):
    nom = models.CharField(max_length=100)
    cognom1 = models.CharField(max_length=100)
    cognom2 = models.CharField(max_length=100, blank=True, null=True)
    correu = models.EmailField(unique=True)
    cursos = models.TextField(blank=True, null=True)  
    moduls = models.TextField(blank=True, null=True)  
    edat = models.IntegerField(blank=True, null=True)  
    rol = models.CharField(max_length=20)
