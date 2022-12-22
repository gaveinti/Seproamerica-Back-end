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
        return JsonResponse({'data':list(qs)},safe=False)

