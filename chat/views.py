import json
from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CanalMensaje,Canal, CanalUsuario
from django.http import HttpResponse,Http404,JsonResponse



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
            texto=data_json["texto"]
        )
        nuevo_mensaje.save()
        
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
@csrf_exempt
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



