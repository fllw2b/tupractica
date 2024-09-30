from django.db import models
from apps.tuPractica.models import Region, Comuna, Carrera


class Usuario(models.Model):
    uid = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    es_estudiante = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Estudiante(models.Model):
    usuario = models.OneToOneField(
        Usuario, on_delete=models.CASCADE, related_name='estudiante')
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    rut = models.CharField(max_length=12)
    region = models.ForeignKey(
        Region, on_delete=models.SET_NULL, null=True)
    comuna = models.ForeignKey(
        Comuna, on_delete=models.SET_NULL, null=True)
    carrera = models.ForeignKey(
        Carrera, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class Empresa(models.Model):
    usuario = models.OneToOneField(
        Usuario, on_delete=models.CASCADE, related_name='empresa')
    nombre_empresa = models.CharField(max_length=255)
    rut = models.CharField(max_length=12)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_empresa
