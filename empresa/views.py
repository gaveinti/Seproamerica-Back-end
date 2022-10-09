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

from empresa.models import usuario
from empresa.serializers import UsuarioSerializer

# Create your views here.
@api_view(['GET', 'POST'])
@csrf_exempt
def usuarioRegistro(request):
    #registrar un nuevo usuario
    if request.method == 'POST':
        usuarioARegistrar_Data = JSONParser().parse(request)
        usuarioARegistrar_Serializer = UsuarioSerializer(data = usuarioARegistrar_Data)
        if usuarioARegistrar_Serializer.is_valid():
            usuarioARegistrar_Serializer.save()
            return JsonResponse(usuarioARegistrar_Serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(usuarioARegistrar_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        usuarios = usuario.objects.all()
        
        nombre = request.GET.get('nombres', None)
        if nombre is not None:
            usuarios = usuarios.filter(nombre_icontains=nombre)
        usuarios_serializer = UsuarioSerializer(usuarios, many=True)
        return JsonResponse(usuarios_serializer.data, safe=False)

#Función para obtener datos de un usuario para validacion en inicio sesion
@api_view(['GET', 'PUT'])
@csrf_exempt
def usuarioInicioSesion(request, correoU):
    #pk = self.kwargs.get('pk')
    #Encontrar usuario por pk (cedula)
    #print(usuario.objects.get())

    try:
        usuarioAEncontrar = usuario.objects.get(correo=correoU)

        #mandar datos para validación
        if request.method == 'GET':
            usuarioAEncontrar_serializer = UsuarioSerializer(usuarioAEncontrar) #El del final es el modelo
            return JsonResponse(usuarioAEncontrar_serializer.data)
        elif request.method == 'PUT':
            usuarioAEncontrar_data = JSONParser().parse(request)
            usuarioAEncontrar_serializer = UsuarioSerializer(usuarioAEncontrar, data=usuarioAEncontrar_data)
            if usuarioAEncontrar_serializer.is_valid():
                usuarioAEncontrar_serializer.save()
                return JsonResponse(usuarioAEncontrar_serializer.data)
            return JsonResponse(usuarioAEncontrar_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except usuario.DoesNotExist:
        return JsonResponse({'message' : 'El usuario no existe'}, status=status.HTTP_404_NOT_FOUND)

