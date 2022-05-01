from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name="InicioEscuela"),
    path('buscar/<tema>/', views.buscar_tema, name="BuscarClase")
]
