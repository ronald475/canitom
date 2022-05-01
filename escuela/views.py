from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Hola mundo")

def buscar_tema(request, tema):
    return render(request, "escuela/buscar.html")