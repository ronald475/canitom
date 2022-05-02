from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio_voluntariado, name="InicioVoluntariado"),
    path("nuevo_voluntario/", views.nuevo_voluntario, name="NuevoVoluntario"),
    path("nuevo_facilitador/", views.nuevo_facilitador, name="NuevoFacilitador"),
    path('buscar/<nombre>/', views.buscar_voluntario, name="BuscarVoluntario"),
    path('buscar/resultados', views.resultados_vol, name="BuscarResultados"),
]
