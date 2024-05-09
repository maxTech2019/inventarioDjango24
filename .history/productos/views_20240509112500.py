from django.shortcuts import render
from .models import Producto

# Create your views here.

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        nombre = 
