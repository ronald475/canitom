from django.shortcuts import render
from .forms import FormVoluntario

def inicio(request):
    return render(request, "voluntariado/inicio.html")

def nuevo_voluntario(request):
    if request.method == "POST":
        ...

    mi_form = FormVoluntario()
    return render(request, "voluntariado/formVol.html", {"form":mi_form})