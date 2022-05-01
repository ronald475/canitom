from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path("nuevo_voluntario/", views.nuevo_voluntario, name="NuevoVoluntario")
]
