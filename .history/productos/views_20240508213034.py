from django.shortcuts import render

# Create your views here.
productos = []

def listar_productos(request):
    return render(request, 'listar_productos.html', {productos})