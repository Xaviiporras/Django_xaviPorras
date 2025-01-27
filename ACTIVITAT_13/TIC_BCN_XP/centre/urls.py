from django.urls import path
from . import views

urlpatterns = [
    path('proff',views.proff, name='proff'),
    path('users',views.users, name='users')
]