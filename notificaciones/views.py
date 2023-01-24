from chat.models import CanalMensaje
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
# Create your views here.

from swapper import load_model

# Send to single device.
from pyfcm import FCMNotification


#built-in signals
from django.db.models.signals import post_save




Notificacion= load_model('notificaciones','Notificacion')
TokenNotificacion= load_model('notificaciones','TokenNotificacion')
Usuario=load_model('empresa','usuario')

@api_view(['GET'])
def obtener_notificaciones_por_usuario(request,usuario_actual):
    if request.method == 'GET':
        qs=Notificacion.objects.filter(destiny=usuario_actual).values()
        return JsonResponse({
            'data':list(qs),
            'cantidad':qs.count()
            },safe=False)

@api_view(['GET'])
def obtener_no_leido(request,usuario_actual):
    if request.method=='GET':
        qs= Notificacion.objects.no_leido().filter(destiny=usuario_actual).values()
        cantidad=qs.count()
        return JsonResponse({
            'data':list(qs),
            'cantidad':cantidad
            },safe=False)


    
@api_view(['GET'])
def marcar_como_leido(request,id):
    if request.method=='GET':
        qs = Notificacion.objects.marcar_como_leido(id)

        return JsonResponse({
            'data':qs,
            },safe=False)
    


@api_view(['POST'])
@csrf_exempt
def guardar_token_movil(request):
    
    if request.method=='POST':
        data=request.data
        user= Usuario.objects.filter(cedula=data['cedula']).first()

        if(user): 
            print("user:",user)
            print("data:",data)
            print("data:",data['token'])
                    
            
            if(TokenNotificacion.objects.filter(token_icontains=data["token"])):
                print("token ya registrado")
            else:
                qs= TokenNotificacion(
                token=data['token'],
                usuario=user
                )
                qs.save()
            
            return JsonResponse({'data':'ok'})

@api_view(['GET'])
def obtener_tokens(request):
    if request.method=='GET':
        qs= TokenNotificacion.objects.all().values_list('token',flat=True)
        print(TokenNotificacion.objects.all().values_list('token'))
        return JsonResponse({'tokens':list(qs)},safe=False)

@api_view(['GET'])

def obtener_token(request,cedula):
    if request.method=='GET':
        qs= TokenNotificacion.objects.filter(usuario_id=cedula).values_list('token',flat=True)
        print(TokenNotificacion.objects.filter(usuario_id=cedula).values_list('token',flat=True))
        return JsonResponse({'res':list(qs)},safe=False)



@api_view(['POST'])
@csrf_exempt  
def notificar_FCM(request):
        if request.method=='POST':
            API_KEY_FCM=request.data['API_KEY_FCM']
            titulo=request.data['titulo']
            descripcion=request.data['descripcion']
            print(API_KEY_FCM)

            token_ids_registration= TokenNotificacion.objects.all().values_list('token',flat=True)
            push_service = FCMNotification(api_key=API_KEY_FCM)

            # Send to multiple devices by passing a list of ids.
            registration_ids = list(token_ids_registration)
            message_title = titulo
            message_body = descripcion
            result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)
            print(result)
            return JsonResponse({'data':'ok'})
 

@api_view(['POST'])
@csrf_exempt 
def notificar_administradores(request):
    if request.method=='POST':
        qs=Usuario.objects.filter(rol=1).values()
        administradores=list(qs)
        contenido=request.data['contenido']
        emisor=request.data['emisor']
        #receptor=request.data['receptor']
        level=request.data['level']        
        for admin in administradores:
            print(admin['correo'])
            Notificacion.objects.notificar_evento(emisor=emisor,receptor=admin['correo'],texto=contenido,level=level)
        
            #return Canal.objects.notify_mensaje(emisor=usuario_actual,receptor=usuario_receptor,texto=data_json["texto"])
            
        
        #Canal.objects.notificar()
        
        #Canal.objects.notify_mensaje(emisor=usuario_receptor,receptor=usuario_actual,texto="Nuevo Mensaje")
        #if(level=="Nuevo mensaje")
        #post_save.connect(notificar(),sender=CanalMensaje)
        return JsonResponse({
            #'emisor':emisor,
            'notificado':True
            #'contenido':contenido,
            #'level':level
            })


@api_view(['POST'])
@csrf_exempt 
def notificar(request):
    if request.method=='POST':
        contenido=request.data['contenido']
        emisor=request.data['emisor']
        receptor=request.data['receptor']
        level=request.data['level']        
        Notificacion.objects.notificar_evento(emisor=emisor,receptor=receptor,texto=contenido,level=level)
            #return Canal.objects.notify_mensaje(emisor=usuario_actual,receptor=usuario_receptor,texto=data_json["texto"])
            
        
        #Canal.objects.notificar()
        
        #Canal.objects.notify_mensaje(emisor=usuario_receptor,receptor=usuario_actual,texto="Nuevo Mensaje")
        #if(level=="Nuevo mensaje")
        #post_save.connect(notificar(),sender=CanalMensaje)
        return JsonResponse({
            'emisor':emisor,
            'receptor':receptor,
            'contenido':contenido,
            'level':level
            })

