from django.db import models

# Create your models here.
class ClienteRegistro(models.Model):
    apellidos = models.CharField(max_length=70, blank=False, default='')
    nombres = models.CharField(max_length=70, blank=False, default='')
    cedula = models.IntegerField(default='')
    fNacimiento = models.DateField(default='')
    sexo = models.CharField(max_length=70, blank=False, default='')
    correo = models.CharField(max_length=70, blank=False, default='')
    telefono = models.IntegerField(default="")
    contrasenha = models.CharField(max_length=70, blank=False, default='')

class ClienteInicioSesion(models.Model):
    correo = models.CharField(max_length=70, blank=False, default='')
    contrasenha = models.CharField(max_length=70, blank=False, default='')

#Probando integración
