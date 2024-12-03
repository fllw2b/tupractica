from rest_framework import serializers
from ..models import AnuncioPractica
from ...usuarios.serializers.empresa_serializer import EmpresaSerializer
from apps.tuPractica.models import Region, Comuna

class AnuncioPracticaSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer(read_only=True)  # Para mostrar detalles de la empresa
    region = serializers.StringRelatedField(read_only=True)  # Muestra el nombre de la región
    comuna = serializers.StringRelatedField(read_only=True)  # Muestra el nombre de la comuna
    requisitos = serializers.StringRelatedField(many=True, read_only=True)  # Muestra los tags relacionados

    class Meta:
        model = AnuncioPractica
        fields = '__all__'
