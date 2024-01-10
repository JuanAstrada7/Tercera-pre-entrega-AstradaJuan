from django.urls import path
from falfajorApp.views import *

urlpatterns = [
   
    path('', inicio, name="Inicio"),
    path('alfajores/', alfajores, name="Alfajores"),
    path('clientes/',clientes, name="Clientes"),
    path('pedidos/', pedidos, name="Pedidos"),
    path('buscar/', buscar),
   
]