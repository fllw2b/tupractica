from rest_framework import serializers
from ..models import Estudiante

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = [
            'id', 'nombres', 'apellidos', 'rut', 'region', 'comuna', 'carrera','usuario',
            'fecha_nacimiento', 'genero', 'direccion', 'telefono', 'foto', 'cv', 'habilidades'
        ]
        depth = 1  # para incluir los detalles de region y comuna
