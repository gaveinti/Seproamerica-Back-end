from django.contrib import admin
from notificaciones.utils.admin import AbstractNotifyAdmin
# Register your models here.
from .models import Notificacion,TokenNotificacion

admin.site.register(Notificacion,AbstractNotifyAdmin)
admin.site.register(TokenNotificacion)