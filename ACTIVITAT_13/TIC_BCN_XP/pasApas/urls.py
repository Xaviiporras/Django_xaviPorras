from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('guardar_sesion',views.guardar_sesion, name='guardar_sesion'),
    path('recuperar_sesion',views.recuperar_sesion, name='recuperar_sesion'),
    path('eliminar_sesion',views.eliminar_sesion, name='eliminar_sesion'),
]