from django.db import models
from apps.tuPractica.models import Region, Comuna, Carrera, Sector


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
    fecha_nacimiento = models.DateField(default='2000-01-01')
    genero = models.CharField(max_length=10, choices=[(
        'M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], default='O')
    direccion = models.CharField(max_length=255, null=True)
    telefono = models.CharField(max_length=20, null=True)
    foto = models.ImageField(
        upload_to='fotos_estudiantes/', null=True, blank=True)  # Opcional

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class Empresa(models.Model):
    usuario = models.OneToOneField(
        Usuario, on_delete=models.CASCADE, related_name='empresa')
    nombre_empresa = models.CharField(max_length=255)
    rut = models.CharField(max_length=12)
    direccion = models.CharField(max_length=255)
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True)
    pagina_web = models.URLField(max_length=255, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    redes_sociales = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nombre_empresa
