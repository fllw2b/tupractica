from django import forms
from .models import AnuncioPractica


class AnuncioPracticaForm(forms.ModelForm):
    class Meta:
        model = AnuncioPractica
        fields = ['titulo', 'ubicacion', 'modalidad',
                  'descripcion', 'requisitos', 'fecha_fin']
