from django.db import models

class USUARIO(models.Model):
    nombreusuario = models.CharField(max_length=100)
    email = models.EmailField()
    contrasena = models.CharField(max_length=100)
    def __str__(self):
        return self.nombreusuario

    
class REGION(models.Model):
     nombre=models.CharField(max_length=50)
     def __str__(self):
        return self.nombre
     
class PROVINCIA(models.Model):
     nombre=models.CharField(max_length=50)
     id_region=models.ForeignKey(REGION, on_delete=models.CASCADE)
     def __str__(self):
        return self.nombre
class COMUNA(models.Model):
     nombrecomuna=models.CharField(max_length=50)
     id_region=models.ForeignKey(PROVINCIA, on_delete=models.CASCADE)
     def __str__(self):
        return self.nombrecomuna
   
class EMPRESA(models.Model):
     nombreEmpresa=models.CharField(max_length=50)
     direccionEMP=models.CharField(max_length=50)
     telefonoEMP=models.CharField(max_length=50)
     email = models.EmailField()
     id_comuna=models.ForeignKey(COMUNA, on_delete=models.CASCADE)
     contrasenaEMP = models.CharField(max_length=100)
     rutEmpresa = models.CharField(max_length=100)
     def __str__(self):
        return self.nombreEmpresa
     
class ANUNCIO(models.Model):
        titulo= models.CharField(max_length=100)
        descripcion = models.CharField(max_length=200)
        modalidad= models.CharField(max_length=100)
        ubicacion= models.CharField(max_length=100)
        requisitos= models.CharField(max_length=200)
        remunerado=models.BooleanField(default=False)
        id_empresa=models.ForeignKey(EMPRESA, on_delete=models.CASCADE)
        def __str__(self):
                return self.titulo