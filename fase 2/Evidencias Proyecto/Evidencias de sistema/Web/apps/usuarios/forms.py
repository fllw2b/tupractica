from django import forms
from .models import Usuario, Estudiante, Empresa, Tag
from apps.tuPractica.models import Region, Comuna, Carrera


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'es_estudiante']


class EstudianteForm(forms.ModelForm):
    habilidades = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control select2-habilidades', 'data-placeholder': 'Selecciona hasta 5 habilidades'}),
        required=False,
        label="Habilidades",
    )

    class Meta:
        model = Estudiante
        fields = [
            'nombres', 'apellidos', 'rut', 'region', 'comuna', 'carrera',
            'telefono', 'cv', 'foto', 'habilidades'
        ]
        widgets = {
            'region': forms.Select(attrs={'class': 'form-control'}),
            'comuna': forms.Select(attrs={'class': 'form-control'}),
            'carrera': forms.Select(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'cv': forms.FileInput(attrs={'class': 'form-control', 'accept': 'application/pdf'}),
            'foto': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }

    def clean_habilidades(self):
        habilidades = self.cleaned_data.get('habilidades')
        if habilidades.count() > 10:
            raise forms.ValidationError("Puedes seleccionar hasta un máximo de 10 habilidades.")
        return habilidades
    
class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nombre_empresa', 'rut', 'direccion', 'sector', 'pagina_web', 'descripcion', 'redes_sociales', 'logo']
        widgets = {
            'nombre_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'sector': forms.Select(attrs={'class': 'form-select'}),
            'pagina_web': forms.URLInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'redes_sociales': forms.URLInput(attrs={'class': 'form-control'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_pagina_web(self):
        pagina_web = self.cleaned_data.get('pagina_web')
        if pagina_web and not pagina_web.startswith(('http://', 'https://')):
            pagina_web = 'http://' + pagina_web
        return pagina_web


