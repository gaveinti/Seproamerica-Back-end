from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
# Create your views here.

from swapper import load_model

# Send to single device.
from pyfcm import FCMNotification



Notificacion= load_model('notificaciones','Notificacion')
TokenNotificacion= load_model('notificaciones','TokenNotificacion')
Usuario=load_model('empresa','usuario')

@api_view(['GET'])
@csrf_exempt
def obtener_notificaciones_por_usuario(request,usuario_actual):
    if request.method == 'GET':
        qs=Notificacion.objects.filter(destiny=usuario_actual).values()
        return JsonResponse({
            'data':list(qs),
            'cantidad':qs.count()
            },safe=False)

@api_view(['GET'])
@csrf_exempt
def obtener_no_leido(request,usuario_actual):
    if request.method=='GET':
        qs= Notificacion.objects.no_leido().filter(destiny=usuario_actual).values()
        cantidad=qs.count()
        return JsonResponse({
            'data':list(qs),
            'cantidad':cantidad
            },safe=False)


    
@api_view(['GET'])
@csrf_exempt
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
                    
            
            qs= TokenNotificacion(
                token=data['token'],
                usuario=user
            )
            qs.save()
            return JsonResponse({'data':'ok'})

@api_view(['GET'])
@csrf_exempt        
def obtener_tokens(request):
    if request.method=='GET':
        qs= TokenNotificacion.objects.all().values_list('token',flat=True)
        print(TokenNotificacion.objects.all().values_list('token'))
        return JsonResponse({'tokens':list(qs)},safe=False)


@api_view(['POST'])
@csrf_exempt  
def notificar(request):
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



