from django.db import models


class Facilitador(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    presentacion = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Voluntario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"