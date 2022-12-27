#ContentType
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

#Timezone
from django.utils import timezone

#load model
from swapper import load_model

#Signals
from notificaciones.signals import notificar

#Django
from django.db.models.query import  QuerySet
from django.db import models
from empresa.models import usuario

# Create your models here.


'''class notificacion(models.Model):
    idNotificacion = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=30)
    contenido = models.TextField()
    leido = models.BooleanField()'''
    
class NotificacionQueryset(models.QuerySet):
    def leido(self, include_deleted=True):
        '''
        Retornar notificaciones leidas en el actual queryset
        '''
        if include_deleted:
            return self.filter(read=True)
    
    def no_leido(self, include_deleted=False):
        '''
        Retornar notificaciones que no han sido leidas en el actual queryset
        '''
        if include_deleted==True:
            return self.filter(read=False)

    def marcar_todo_como_leido(self,destiny):
        '''
        Marcar todas las notificaciones como leidas en el actual queryset
        '''
        qs=self.read(False)
        if destiny:
            qs=qs.filter(destiny=destiny)
        return qs.update(read=True)

class AbstractNotificacionManager(models.Manager):
    def get_queryset(self):
        return self.NotificacionQueryset(self.Model,using=self._db)

class AbstractNotificacion(models.Model):
    

    class Levels(models.TextChoices):
        success='Success','success'
        info='Info','info'
        wrong='Wrong','wrong'

    level=models.CharField(choices=Levels.choices,max_length=20,default=Levels.info)

    destiny=models.ForeignKey(usuario,on_delete=models.CASCADE,related_name='notificaciones',blank=True,null=True)

    actor_content_type=models.ForeignKey(ContentType,related_name='notificar_actor',on_delete=models.CASCADE)
    object_id_actor=models.PositiveIntegerField()
    actor=GenericForeignKey('actor_content_type','object_id_actor')

    verbo=models.CharField(max_length=220)
    timestamp=models.DateTimeField(default=timezone.now,db_index=True)
    
    read=models.BooleanField(default=False)

    publico=models.BooleanField(default=True)

    eliminado=models.BooleanField(default=False)

    objects=NotificacionQueryset.as_manager()

    class Meta:
        abstract=True

    #def __str__(self):
    #    return 'Actor: {}'.format(self.actor)


    def notify_signals(verbo,**kwargs):
        '''
            Funcion de controlador para crear instancia de notificacion
            tras una llamada de señal de accion
        '''
        destiny=kwargs.pop('destiny')
        actor=kwargs.pop('sender')

        publico=bool(kwargs.pop('publico',True))
        timestamp=kwargs.pop('timestamp',timezone.now())
        Notify=load_model('notificaciones','Notificacion')
        levels=kwargs.pop('level',Notify.Levels.info)

        #if isinstance(destiny,Group):
        #    destiny=destiny.user_set.all()
        if isinstance(destiny,(QuerySet,list)):
            destinies=destiny
        else:
            destinies=[destiny]

        new_notify=[]
        for destiny in destinies:
            notificacion=Notify(
                destiny=destiny,
                actor_content_type= ContentType.objects.get_for_model(actor),
                object_id_actor=actor.pk,
                verbo=str(verbo),
                publico=True,
                timestamp=timestamp,
                level=levels
            )

            notificacion.save()
            new_notify.append(notificacion)

        return new_notify

    notificar.connect(notify_signals,dispatch_uid='notificaciones.models.Notificacion')