from rest_framework import serializers
from ..models import Estudiante, Region, Carrera, Comuna

class EstudianteSerializer(serializers.ModelSerializer):
    foto = serializers.SerializerMethodField()

    class Meta:
        model = Estudiante
        fields = '__all__'
        depth = 1
    def get_foto(self, obj):
        if obj.foto:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.foto.url) if request else obj.foto.url
        return None


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'nombre']

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ['id', 'nombre']

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = ['id', 'nombre']