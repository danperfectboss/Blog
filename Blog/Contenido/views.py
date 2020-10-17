from django.shortcuts import render
# from Contenido.models import *

# Create your views here.
def prueba(request):
    return render(request, 'html_estatico/index.html')
    