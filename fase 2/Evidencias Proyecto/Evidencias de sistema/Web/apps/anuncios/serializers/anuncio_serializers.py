from rest_framework import serializers
from ..models import AnuncioPractica
from ...usuarios.serializers.empresa_serializer import EmpresaSerializer
from apps.tuPractica.models import Region, Comuna

class AnuncioPracticaSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer(read_only=True)
    region_id = serializers.IntegerField(source='region.id', read_only=True)
    comuna = serializers.StringRelatedField(read_only=True)
    requisitos = serializers.SerializerMethodField()
    region_nombre = serializers.CharField(source='region.nombre', read_only=True) 
    
    class Meta:
        model = AnuncioPractica
        fields = '__all__'
    
    def get_requisitos(self, obj):
        return [tag.nombre for tag in obj.requisitos.all()]