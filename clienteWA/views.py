from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
# Para agregar mensaje y verificar la conexion
from django.contrib import messages

from clienteWA.models import ClienteInicioSesion, ClienteRegistro
from clienteWA.serializers import ClienteInicioSesionSerializer, ClienteRegistroSerializer


# Create your views here.
@csrf_exempt
def clienteInicioSesionApi(request):
    if request.method == 'POST':
        cliente_IS_data = JSONParser().parse(request)
        cliente_IS_serializer = ClienteInicioSesionSerializer(data=cliente_IS_data)
        if cliente_IS_serializer.is_valid():
            cliente_IS_serializer.save()
            return JsonResponse("Agregado exitosamente", safe=False)
        return JsonResponse("Agregado fallido", safe=False)
