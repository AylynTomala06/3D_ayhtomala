from django.urls import path
from.views import inicio, ulectorf, alquilerf,agregarlibro

urlpatterns = [
    path('', inicio, name='inicio'),
    path('lectores/',ulectorf, name='ulectof'),
    path('alquiler/', alquilerf, name='alquilerf'),
    path('agregarlibro/',agregarlibro, name='agregarlibro'),
]