from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
# Create your views here.

from swapper import load_model

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
def guardarTokenMovil(request):
    
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
            
