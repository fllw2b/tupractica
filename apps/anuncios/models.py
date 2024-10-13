from django.db import models
from apps.usuarios.models import Empresa, Estudiante
from apps.tuPractica.models import Region, Comuna

# Create your models here.
class AnuncioPractica(models.Model):
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, related_name='anuncios')
    titulo = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True)
    ubicacion = models.CharField(max_length=255)  # Campo de ubicación
    modalidad = models.CharField(
        max_length=20,
        choices=[
            ('remoto', 'Remoto'),
            ('hibrido', 'Híbrido'),
            ('presencial', 'Presencial')
        ],
        default='remoto'
    )
    descripcion = models.TextField()
    requisitos = models.TextField(null=True, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True, editable=False)
    fecha_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo


class Postulacion(models.Model):
    estudiante = models.ForeignKey(
        Estudiante, on_delete=models.CASCADE, related_name='postulaciones')
    anuncio = models.ForeignKey(
        AnuncioPractica, on_delete=models.CASCADE, related_name='postulantes')
    fecha_postulacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.estudiante.usuario.email} - {self.anuncio.titulo}"
