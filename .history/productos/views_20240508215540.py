from django.shortcuts import render
from .models import

# Create your views here.

def listar_productos(request):
    productos = 
    return render(request, 'listar_productos.html', {'productos':productos})