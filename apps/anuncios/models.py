from django.db import models
from apps.usuarios.models import Empresa, Estudiante, Tag
from apps.tuPractica.models import Region, Comuna
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your models here.
class AnuncioPractica(models.Model):
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, related_name='anuncios')
    titulo = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True)
    ubicacion = models.CharField(max_length=255)
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
    requisitos = models.ManyToManyField(Tag, related_name='anuncios_practica', blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True, editable=False)
    fecha_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo


class Postulacion(models.Model):
    ESTADOS_POSTULACION = [
        ('En revisión', 'En revisión'),
        ('Aprobado', 'Aprobado'),
        ('Rechazado', 'Rechazado'),
    ]

    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='postulaciones')
    anuncio = models.ForeignKey(AnuncioPractica, on_delete=models.CASCADE, related_name='postulantes')
    fecha_postulacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS_POSTULACION, default='En revisión')

    def enviar_correo_estado(self):
        # se llama al html
        html_content = render_to_string('anuncios/notificacion_postulacion.html', {
            'estudiante': self.estudiante,
            'anuncio': self.anuncio,
            'estado': self.estado,
            'url_postulaciones': 'http://tupractica.com/postulaciones',
            'year': 2024,
        })

        # configuracion del correo
        asunto = f"Estado de tu postulación a {self.anuncio.titulo}"
        email = EmailMultiAlternatives(
            subject=asunto,
            body="",
            from_email="tupractica27@gmail.com",
            to=[self.estudiante.usuario.email]
        )
        email.attach_alternative(html_content, "text/html")
        email.send()