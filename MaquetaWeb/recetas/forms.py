from django import forms
from .models import * 


class CrearRecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['nombre', 'categoria', 'ingredientes', 'preparacion']


class BuscarRecetaForm(forms.Form):
    nombre = forms.CharField(required=False)
    categoria = forms.CharField(required=False)
    ingredientes = forms.CharField(required=False)
    
    