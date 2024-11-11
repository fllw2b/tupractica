from django.db import models


class Region(models.Model):
    id = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Comuna(models.Model):
    id = models.AutoField(primary_key=True)  
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.nombre} ({self.region})"


class Carrera(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Sector(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
