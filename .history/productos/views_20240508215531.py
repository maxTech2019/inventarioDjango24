from django.shortcuts import render

# Create your views here.

def listar_productos(request):
    productos = 
    return render(request, 'listar_productos.html', {'productos':productos})