import json
from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CanalMensaje,Canal, CanalUsuario
from notificaciones import models
from django.http import HttpResponse,Http404,JsonResponse

#built-in signals
from django.db.models.signals import post_save

#signals
from notificaciones.signals import notificar




from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view

from empresa.models import usuario


from rest_framework.parsers import JSONParser 
from django.core import serializers

# Create your views here.

@api_view(['GET', 'POST'])
@csrf_exempt
def verificar_y_crear_canal(request,id_servicio,servicio,usuario_receptor,usuario_actual):


    if request.method == 'POST':
        #mensaje_por_canal=JSONParser().parse(request.data)
        data_json=dict(request.data)
        print(data_json)
        print("=============================")
        canal_c=Canal.objects.get(id=data_json["canal"])
        usuario_canal=usuario.objects.get(correo=data_json["usuario"])
        nuevo_mensaje=CanalMensaje(
            canal=canal_c,
            usuario=usuario_canal,
            texto=data_json["texto"],
            check_leido=data_json["check_leido"]

        )
        
        #def notificar(**kwargs):
        #    return models.Notificacion.objects.notificar_evento(emisor=usuario_actual,receptor=usuario_receptor,texto=data_json["texto"])
            #return Canal.objects.notify_mensaje(emisor=usuario_actual,receptor=usuario_receptor,texto=data_json["texto"])
            
        
        #Canal.objects.notificar()
        
        #Canal.objects.notify_mensaje(emisor=usuario_receptor,receptor=usuario_actual,texto="Nuevo Mensaje")
        nuevo_mensaje.save()
        #post_save.connect(notificar(),sender=CanalMensaje)

        #CanalMensaje.notificar_nuevo_mensaje(usuario_actual,usuario_receptor,text="Nuevo Mensaje")
        #notificar.send(sender=usuario_actual,destiny=usuario_receptor,verbo="Nuevo Mensaje",level='success')


        #Envio de notificacion cuando se agrega un mensaje
        '''def notify_mensaje(sender,instance,created,**kwargs):
            notificar.send(instance.usuario,destiny=instance.usuario,verbo=instance.texto,level='success')
        post_save.connect(notify_mensaje,sender=CanalMensaje)'''
        '''
        def notify_mensaje(sender,instance,created,**kwargs):
            receptor=usuario.objects.filter(correo=usuario_receptor)
            print(receptor)
            notificar.send(instance.usuario,destiny=receptor.first(),verbo=instance.texto,level='success')
        post_save.connect(notify_mensaje,sender=CanalMensaje)

        '''

   
        #CanalMensaje.objects.create()
        return JsonResponse(data_json)
        

    elif request.method == 'GET':

        
        mi_username=usuario_actual

        canal,_= Canal.objects.obtener_o_crear_canal_ms(mi_username,usuario_receptor,servicio,id_servicio)
        #canal="hola"
        if canal == None:
            return JsonResponse({'mensaje':'Canal no creado','status':'Error'})
        
        nombre_receptor=usuario.objects.filter(correo=usuario_receptor).first().nombres
        apellido_receptor=usuario.objects.filter(correo=usuario_receptor).first().apellidos
        
        perfil_receptor=nombre_receptor+" "+apellido_receptor
        
        if usuario_receptor == mi_username:
            return JsonResponse({"mensaje":"Canal consigo mismo no puede crearse"})

        
        mensajes=CanalMensaje.obtener_data_mensaje_usuarios(canal.id)

        
        print()
        print("servicio",canal.servicio)
        return JsonResponse({
            'canal':canal.id,
            'servicio':canal.servicio,
            'id_servicio':canal.id_servicio,
            'receptor':usuario_receptor,
            'usuario_logeado':mi_username,
            'perfil_receptor':perfil_receptor,
            'mensajes':mensajes
            
            })


@api_view(['GET'])
def obtener_canales_usuario_actual(request,usuario_actual):

    qs=usuario.objects.filter(correo=usuario_actual)
    if not qs.exists():
        return JsonResponse({"mensaje":"No esta autenticado","status":"Error"})


    canales_s=Canal.objects.filter(usuarios__correo=usuario_actual).values("id","servicio")

    canales_s=list(canales_s.order_by("tiempo"))
    canales_con_todos_los_mensajes_por_usuario=[]
    for canal in canales_s:

        usuarios_Canal = list(Canal.objects.filter(id=canal["id"]).values(
            "canalusuario__usuario__correo",
            "canalusuario__usuario__nombres",
            "canalusuario__usuario__apellidos"
            ))
        usuarios_canal = [
            [
            usuarios_Canal[0]["canalusuario__usuario__correo"],  
            usuarios_Canal[0]["canalusuario__usuario__nombres"]+" "+usuarios_Canal[0]["canalusuario__usuario__apellidos"],

        ],
            [
            usuarios_Canal[1]["canalusuario__usuario__correo"],  
            usuarios_Canal[1]["canalusuario__usuario__nombres"]+" "+usuarios_Canal[1]["canalusuario__usuario__apellidos"],

            ]
            
        ]
  

        mensajes=CanalMensaje.obtener_data_mensaje_usuarios(canal["id"])
        
        canales_con_todos_los_mensajes_por_usuario.append(
            {'CANAL_ID':canal["id"],'usuarios_canal':usuarios_canal,'servicio':canal["servicio"],'mensajes':mensajes}
        )
    #print(canales_con_todos_los_mensajes_por_usuario)
   
    return JsonResponse(canales_con_todos_los_mensajes_por_usuario,safe=False)


@api_view(['GET', 'POST'])
@csrf_exempt
def actualizar_sms_leido(request,id_mensaje,check_leido):
    if request.method == 'GET':
        qs = CanalMensaje.verificar_leido(id_mensaje,check_leido)
    
        return JsonResponse({
            'data':qs,
            },safe=False)

'''

@api_view(['GET', 'POST'])
@csrf_exempt
def obtener_mensajes(request):
    if request.method == 'GET':
        mensajes = Mensaje.objects.all()
        
        mensajes_serializer = MensajeSerializer(mensajes, many=True)
    

        return JsonResponse(
            {'data':"hola",
            'mensajes':mensajes_serializer.data}, 
            safe=False)'''



