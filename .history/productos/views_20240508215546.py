from django.shortcuts import render
from .models import Producto

# Create your views here.

def listar_productos(request):
    productos = Producto.
    return render(request, 'listar_productos.html', {'productos':productos})