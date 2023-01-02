from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
# Create your views here.

from swapper import load_model

Notificacion= load_model('notificaciones','Notificacion')

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
    

