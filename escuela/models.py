from django.db import models


class Clase(models.Model):
    titulo = models.CharField(max_length=40)
    tema = models.CharField(max_length=40)
    contenido = models.TextField()
    fecha = models.DateField()
