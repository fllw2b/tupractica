from django.db import models
from apps.tuPractica.models import Region, Comuna, Carrera, Sector

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(
                'Por favor, ingrese un correo valido')
        email = self.normalize_email(email)
        usuario = self.model(email=email, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    es_estudiante = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

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
        upload_to='fotos_estudiantes/', null=True, blank=True) 
    cv = models.FileField(upload_to='cvs/', null=True, blank=True)
    habilidades = models.ManyToManyField('Tag', related_name='estudiantes', blank=True, limit_choices_to=10)

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
    descripcion = models.TextField(
        max_length=1000, 
        null=True,
        blank=True,
        help_text="Una breve descripción sobre la empresa (máx. 1000 caracteres)."
    )
    redes_sociales = models.URLField(max_length=255, null=True, blank=True)
    logo = models.ImageField(upload_to='logos_empresa/', null=True, blank=True) 

    def __str__(self):
        return self.nombre_empresa


class Tag(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre