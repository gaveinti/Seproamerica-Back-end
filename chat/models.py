from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

from django.apps import apps
import uuid

from django.db.models import Count
from empresa.models import usuario

User= settings.AUTH_USER_MODEL
#User = usuario
# Create your models here.
class ModelBase(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,db_index=True,editable=False)
    tiempo = models.DateTimeField(auto_now_add=True)
    actualizar= models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class CanalMensaje(ModelBase):
    canal= models.ForeignKey("Canal", on_delete=models.CASCADE)
    usuario=models.ForeignKey(usuario,on_delete=models.CASCADE)
    texto=models.TextField()

class CanalUsuario(ModelBase):
    canal=models.ForeignKey("Canal",null=True,on_delete=models.SET_NULL)
    usuario= models.ForeignKey(usuario,on_delete=models.CASCADE)


class  CanalQuerySet(models.QuerySet):

    def solo_uno(self):
        return self.annotate(num_usuarios=Count("usuarios")).filter(num_usuarios=1)

    def solo_dos(self):
        return self.annotate(num_usuarios=Count("usuarios")).filter(num_usuarios=2)

    def filtrar_por_correo(self,correo):
        return self.filter(canalusuario__usuario__correo=correo)


class CanalManager(models.Manager):
    def get_queryset(self,*args,**kwards):
        return CanalQuerySet(self.model,using=self._db) 

    def filtrar_ms_por_privado(self,correo_a,correo_b):
        return self.get_queryset().solo_dos().filtrar_por_correo(correo_a).filtrar_por_correo(correo_b)

    def obtener_o_crear_canal_usuario_actual(self,correo):
        qs=self.get_queryset().solo_uno().filtrar_por_correo(correo)
        if qs.exists():
            return qs.order_by("tiempo").first(),False
        
        canal_obj=Canal.objects.create()
        CanalUsuario.objects.create(usuario=correo,canal=canal_obj)
        return canal_obj,True




    def obtener_o_crear_canal_ms_por_correo(self,correo_a,correo_b):
        qs=self.filtrar_ms_por_privado(correo_a,correo_b)
        if qs.exists():
            return qs.order_by("tiempo").first(),False #obj, Created
        correo_a,correo_b=None,None
        try:
            correo_a=usuario.objects.get(correo=correo_a)
        except usuario.DoesNotExist :
            return None,False
        
        try:
            correo_b=usuario.objects.get(correo=correo_b)

        except usuario.DoesNotExist :
            return None,False
        
        if (correo_a==None or correo_b==None):
            return None, False

        obj_canal=Canal.objects.create()
        canal_usuario_a= CanalUsuario(usuario=correo_a,canal=obj_canal)
        canal_usuario_b= CanalUsuario(usuario=correo_b,canal=obj_canal)
        CanalUsuario.objects.bulk_create([canal_usuario_a,canal_usuario_b])

        return obj_canal, True

    def obtener_o_crear_canal_ms(self,username_a,username_b):
        qs=self.filtrar_ms_por_privado(username_a,username_b)
        if qs.exists():
            return qs.order_by("tiempo").first(),False #obj, Created

        User= apps.get_model("auth",model_name='User')
        usuario_a,usuario_b=None,None

        try:
            usuario_a=User.objects.get(username=username_a)
        except User.DoesNotExist :
            return None,False
        
        try:
            usuario_b=User.objects.get(username=username_b)

        except User.DoesNotExist :
            return None,False
        
        if (usuario_a==None or usuario_b==None):
            return None, False

        obj_canal=Canal.objects.create()
        canal_usuario_a= CanalUsuario(usuario=usuario_a,canal=obj_canal)
        canal_usuario_b= CanalUsuario(usuario=usuario_b,canal=obj_canal)
        CanalUsuario.objects.bulk_create([canal_usuario_a,canal_usuario_b])

        return obj_canal, True

class Canal(ModelBase):
    #para 1 o mas usuarios conectados

    usuarios=models.ManyToManyField(usuario,blank=True,through=CanalUsuario)
    objects=CanalManager()