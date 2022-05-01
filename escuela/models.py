from django.db import models


class Facilitador(models.Model):
    titulo = models.CharField(max_length=40)
    tema = models.CharField(max_length=40)
    contenido = models.TextField()
    fecha = models.DateField()
