from django.contrib import admin
from .models import usuario,rol,personalOperativo,personalAdministrativo

admin.site.register(usuario)
admin.site.register(rol)
admin.site.register(personalAdministrativo)
admin.site.register(personalOperativo)