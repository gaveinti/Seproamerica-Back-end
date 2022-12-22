from notificaciones.utils.models import AbstractNotificacion
from django.db import models
from empresa.models import usuario
class Notificacion(AbstractNotificacion):


    class Meta(AbstractNotificacion.Meta):
        abstract=False


class TokenNotificacion(models.Model):
    usuario=models.ForeignKey(usuario, on_delete=models.CASCADE)
    token=models.TextField()