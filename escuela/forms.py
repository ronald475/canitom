from django import forms


class FormClase(forms.Form):
    titulo = forms.CharField(max_length=40)
    tema = forms.CharField(max_length=40)
    contenido = forms.CharField(widget=forms.Textarea)
    fecha = forms.DateField()
