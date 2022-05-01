from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name="InicioVoluntariado"),
    path("nuevo_voluntario/", views.nuevo_voluntario, name="NuevoVoluntario")
]
