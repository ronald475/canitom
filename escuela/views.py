from django.shortcuts import render
from django.http import HttpResponse
from escuela.models import Clase

def inicio(request):
    return HttpResponse("Hola mundo")

def buscar_tema(request, tema):
    if request.GET.get("titulo"):
        titulo=request.GET.get("titulo")
        clases= Clase.objects.filter(titulo__icontains=titulo, tema=tema)
        return render(request, "escuela/resultado_buscar.html", {"clases":clases})

    return render(request, "escuela/buscar.html")