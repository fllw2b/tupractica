from django import forms
from .models import AnuncioPractica
from apps.usuarios.models import Tag

class AnuncioPracticaForm(forms.ModelForm):
    requisitos = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control select2-requisitos', 'data-placeholder': 'Selecciona hasta 10 habilidades'}),
        required=False,
        label="Requisitos (Habilidades)"
    )

    class Meta:
        model = AnuncioPractica
        fields = [
            'titulo', 'ubicacion', 'modalidad', 'descripcion', 'requisitos', 'fecha_fin'
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'modalidad': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean_requisitos(self):
        requisitos = self.cleaned_data.get('requisitos')
        if requisitos.count() > 10:
            raise forms.ValidationError("Puedes seleccionar hasta un máximo de 10 habilidades.")
        return requisitos
