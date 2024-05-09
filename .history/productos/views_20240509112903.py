from django.shortcuts import render, redirect
from .models import Producto

# Create your views here.

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad')
        producto_nuevo = Producto(nombre=nombre, precio=precio, cantidad=cantidad)
        producto_nuevo.save()
        return.redirect