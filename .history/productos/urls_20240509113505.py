from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_productos, name='rlistar_productos'),
    path('agregar/', views.agregar_producto, name='agregar_productos'),
]
