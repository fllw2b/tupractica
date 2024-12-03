from rest_framework import serializers
from ..models import Postulacion
from .anuncio_serializers import AnuncioPracticaSerializer

class PostulacionSerializer(serializers.ModelSerializer):
    anuncio = AnuncioPracticaSerializer(read_only=True)  #para mostrar los detalles del anucnio
    estudiante = serializers.StringRelatedField(read_only=True)  # se muestra la informacion basica del estudiante

    class Meta:
        model = Postulacion
        fields = '__all__'
