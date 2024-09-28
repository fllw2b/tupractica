from rest_framework.serializers import ModelSerializer
from Inicio.models import *

class USUARIOSerializer(ModelSerializer):
    class Meta:
        model=USUARIO
        fields=['id','nombreusuario','email','contrasena']
        
class REGIONSerializer(ModelSerializer):
    class Meta:
        model=REGION
        fields=['id','nombre']

class PROVINCIASerializer(ModelSerializer):
    class Meta:
        model=PROVINCIA
        fields=['id','nombre','id_region']

class COMUNASerializer(ModelSerializer):
    class Meta:
        model=COMUNA
        fields=['id','nombrecomuna', 'id_region']

class EMPRESASerializer(ModelSerializer):
    class Meta:
        model=EMPRESA
        fields=['id','nombreEmpresa', 'direccionEMP', 'telefonoEMP', 'email','id_comuna','contrasenaEMP','rutEmpresa']
