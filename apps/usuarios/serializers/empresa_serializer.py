from rest_framework import serializers
from ..models import Empresa

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = [
            'id', 'nombre_empresa', 'rut', 'direccion', 'sector',
            'pagina_web', 'descripcion', 'redes_sociales'
        ]
        depth = 1 
