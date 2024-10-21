from django import forms
from .models import Usuario, Estudiante, Empresa
from apps.tuPractica.models import Region, Comuna, Carrera


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'es_estudiante']


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombres', 'apellidos', 'rut', 'region', 'comuna', 'carrera']
        widgets = {
            'region': forms.Select(attrs={'class': 'form-control'}),
            'comuna': forms.Select(attrs={'class': 'form-control'}),
            'carrera': forms.Select(attrs={'class': 'form-control'}),
        }


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nombre_empresa', 'rut', 'direccion']
        widgets = {
            'nombre_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }
