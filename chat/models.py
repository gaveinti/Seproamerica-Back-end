from django.db import models
from django.conf import settings

from django.apps import apps
import uuid

from django.db.models import Count

from empresa.models import usuario

#User= settings.AUTH_USER_MODEL
User = usuario
# Create your models here.










class ModelBase(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, db_index=True, editable=False)
    tiempo = models.DateTimeField(auto_now_add=True)
    actualizar = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Mensaje(models.Model):
    canal = models.ForeignKey("Canal", on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    





class CanalMensaje(ModelBase):
    canal = models.ForeignKey("Canal", on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()



    def obtener_data_mensaje_usuarios(id_canal):
        qs = CanalMensaje.objects.filter(
            canal_id=id_canal).values("canal__servicio","texto", "usuario","tiempo","usuario__rol","usuario__correo")
        usuarios_Canal = Canal.objects.filter(
            id=id_canal).values("canalusuario__usuario__correo")

        data=Canal.objects.filter(id=id_canal).values(
            "id",
            "canalmensaje__texto",
            "tiempo",
            "canalmensaje__usuario__correo",
            "canalusuario__usuario__rol",
            "canalusuario__usuario__correo"
            

        ).order_by("tiempo")

        print("CONSULTAA",data)
        mensajes = list(qs.order_by("tiempo"))
        # mensajes=Canal.objects.obtener_todos_mensajes_por_canal(id_canal)
        for sms in mensajes:
            data_usuario=usuario.objects.filter(cedula=sms["usuario"]).values().first()
            nombre = data_usuario["nombres"]
            apellido = data_usuario["apellidos"]
            perfil = nombre+" "+apellido
            sms["nombre_perfil"] = perfil
            sms["usuarios_canal"] = [usuarios_Canal[0]["canalusuario__usuario__correo"],
                                     usuarios_Canal[1]["canalusuario__usuario__correo"]]

        return list(mensajes)



    def __str__(self):
        return str(self.canal)


class CanalUsuario(ModelBase):
    canal = models.ForeignKey("Canal", null=True, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.canal)


class CanalQuerySet(models.QuerySet):

    def solo_uno(self):
        return self.annotate(num_usuarios=Count("usuarios")).filter(num_usuarios=1)

    def solo_dos(self):
        return self.annotate(num_usuarios=Count("usuarios")).filter(num_usuarios=2)

    def filtrar_por_username(self, username):
        return self.filter(canalusuario__usuario__correo=username)

    def filtrar_por_servicio(self, _servicio, usuario_a, usuario_b):
        return self.filtrar_por_username(usuario_a).filtrar_por_username(usuario_b).filter(servicio=_servicio)
    




class CanalManager(models.Manager):
    def get_queryset(self, *args, **kwards):
        return CanalQuerySet(self.model, using=self._db)

    def filtrar_ms_por_privado(self, username_a, username_b, servicio):
        return self.get_queryset().solo_dos().filtrar_por_servicio(servicio, username_a, username_b)



    def obtener_o_crear_canal_ms(self, username_a, username_b, servicio):
        qs = self.filtrar_ms_por_privado(username_a, username_b, servicio)
        if qs.exists():
            return qs.order_by("tiempo").first(), False  # obj, Created

        usuario_a, usuario_b = None, None

        try:
            usuario_a = usuario.objects.get(correo=username_a)
        except usuario.DoesNotExist:
            return None, False

        try:
            usuario_b = usuario.objects.get(correo=username_b)

        except usuario.DoesNotExist:
            return None, False

        if (usuario_a == None or usuario_b == None):
            return None, False

        obj_canal = Canal.objects.create(servicio=servicio)
        canal_usuario_a = CanalUsuario(usuario=usuario_a, canal=obj_canal)
        canal_usuario_b = CanalUsuario(usuario=usuario_b, canal=obj_canal)
        CanalUsuario.objects.bulk_create([canal_usuario_a, canal_usuario_b])

        return obj_canal, True

    '''def obtener_todos_los_canales(self):
        datos_procesados = []
        qs = Canal.objects.all().values("id").order_by("tiempo")

        lista_canales = list(qs)

        for canal in lista_canales:

            ms = CanalMensaje.objects.filter(canal_id=str(canal["id"])).values(
                "tiempo", "texto", "usuario_id").first()
            if (True):
                p_usuario = usuario.objects.filter(cedula=str(ms["usuario_id"])).first(
                ).nombres+" " + usuario.objects.filter(cedula=str(ms["usuario_id"])).first().apellidos

                t = ms["tiempo"]
                tiempo_envio = "%s:%s:%s" % (t.hour, t.month, t.second)
                fecha_envio = "%s/%s/%s" % (t.day, t.month, t.year)
                data = {
                    'usuario': p_usuario,
                    "id_canal": canal["id"],
                    "id_usuario": ms["usuario_id"],
                    'ultimo_mensaje': ms["texto"],
                    "tiempo_envio": tiempo_envio,
                    "fecha_envio": fecha_envio,
                }

                datos_procesados.append(data)

        return datos_procesados


'''
    def obtener_datos_usuario(id_usuario):
        qs =usuario.objects.filter(cedula=id_usuario)  
        return qs


class Canal(ModelBase):
    # para 1 o mas usuarios conectados
    servicio_CHOICES = (("Custodia", "Custodia Armada"), ("Transporte", "Transporte de productos"),
                        ("Chofer", "Chofer seguro"), ("Guardia", "Guardia de seguridad"))
    servicio = models.CharField(max_length=23, choices=servicio_CHOICES)
    usuarios = models.ManyToManyField(User, blank=True, through=CanalUsuario)
    objects = CanalManager()
