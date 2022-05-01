from tkinter.tix import Form
from django import forms
from django.db import models

class FormVoluntario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()