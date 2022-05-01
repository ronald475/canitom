from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Hola mundo")

def nuevo_voluntario(request):
    return render(request, "voluntariado/formVol.html")