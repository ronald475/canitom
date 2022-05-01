from django.shortcuts import render, redirect

from voluntariado.models import Voluntario
from .forms import FormVoluntario

def inicio(request):
    return render(request, "voluntariado/inicio.html")

def nuevo_voluntario(request):
    if request.method == "POST":
        mi_form = FormVoluntario(request.POST)
        if mi_form.is_valid():
            info=mi_form.cleaned_data
            voluntario= Voluntario(
                nombre = info["nombre"],
                apellido = info["apellido"],
                email = info["email"],
            )
            voluntario.save()
            return redirect("InicioVoluntariado")

    mi_form = FormVoluntario()

    return render(request, "voluntariado/formVol.html", {"form":mi_form})