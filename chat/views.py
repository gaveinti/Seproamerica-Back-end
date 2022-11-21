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
def verificar_y_crear_canal(request,servicio,usuario_receptor,usuario_actual):


    if request.method == 'POST':
        #mensaje_por_canal=JSONParser().parse(request.data)
        data_json=dict(request.data)
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

        canal,_= Canal.objects.obtener_o_crear_canal_ms(mi_username,usuario_receptor,servicio)
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
            'receptor':usuario_receptor,
            'usuario_logeado':mi_username,
            'perfil_receptor':perfil_receptor,
            'mensajes':mensajes
            
            })

@api_view(['GET'])
@csrf_exempt
def obtener_canales_usuario_actual(request,usuario_actual):
    #usuario logeado 
    #mi_username = request.session["USER_LOGGED"]["correo"]
    mi_username= usuario_actual

    qs=usuario.objects.filter(correo=mi_username)
    if not qs.exists():
        return JsonResponse({"mensaje":"No esta autenticado","status":"Error"})

    #canal,created= Canal.objects.obtener_o_crear_canal_ms(mi_username,username)
    #if created:
    #    print("Frue creado!")
    #Usuarios_Canal=canal.canalusuario_set.all().values("usuario__correo")
    #print("usuariossss")

    canales_s=Canal.objects.filter(usuarios__correo=mi_username).values("id","servicio")

    canales_s=list(canales_s.order_by("tiempo"))
    canales_con_todos_los_mensajes_por_usuario=[]
    for canal in canales_s:
        mensajes=CanalMensaje.obtener_data_mensaje_usuarios(canal["id"])
        
        canales_con_todos_los_mensajes_por_usuario.append(
            {'CANAL_ID':canal["id"],'servicio':canal["servicio"],'mensajes':mensajes}
        )
    #print(canales_con_todos_los_mensajes_por_usuario)

    return JsonResponse({
            'canales':canales_con_todos_los_mensajes_por_usuario
            })



@csrf_exempt
def get_all_mensajes(request):
    if request.method == 'GET':
        #mensajes= CanalMensaje.obtener_data_formato_general()
        mensajes= Canal.objects.obtener_todos_los_canales()
        return JsonResponse({'mensajes': mensajes})

