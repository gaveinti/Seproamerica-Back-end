from django.contrib import admin
from .models import  * #usuario,rol,personalOperativo, personalAdministrativo,mobil 

admin.site.register(usuario)
admin.site.register(rol)
admin.site.register(personalAdministrativo)
admin.site.register(personalOperativo)
admin.site.register(mobil)
admin.site.register(equipamiento)
#admin.site.register(tipoEquipamiento)
admin.site.register(sucursal)
