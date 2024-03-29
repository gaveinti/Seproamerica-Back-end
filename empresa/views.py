from http.client import HTTPResponse
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

from empresa.models import usuario,personalOperativo, estadoPedido, vehiculo, mobil, candado, armamento, servicio, pedido, sucursal
from empresa.serializers import UsuarioSerializer, vehiculosSerializer, PersonalOperativoSerializer, candadosSerializer,MobilSerializer, armamentosSerializer, ServicioSerializer, PedidoSerializer, ClienteSerializer, PersonalAdministrativoSerializer, PersonalOperativoSerializer
from empresa.models import usuario,personalOperativo, detallePerfilOp, vehiculo, mobil, candado, armamento, cliente, tipoServicio
from empresa.serializers import *

import json

#--------------------------------------------- API's para administrador -------------------------------------------------

#API para luego de registrar usuario, tambien registrar cliente
@api_view(['GET', 'POST'])
@csrf_exempt
def adminRegistro(request):
    if request.method == 'POST':
        admin_A_Registrar_Data = JSONParser().parse(request)
        admin_A_Registrar_Serializer = PersonalAdministrativoSerializer(data=admin_A_Registrar_Data )
        if admin_A_Registrar_Serializer.is_valid():
            admin_A_Registrar_Serializer.save()
            return JsonResponse(admin_A_Registrar_Serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(admin_A_Registrar_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#API para obtener un cliente de la tabla de clientes a partir de la cédula
@api_view(['GET'])
def obtenerAdministrador(request, cedula_Admin_or_id):

    try: 
        admin_A_Encontrar = personalAdministrativo.objects.get(cedula=cedula_Admin_or_id)
        if request.method == 'GET':
            admin_A_Encontrar_serializer = PersonalAdministrativoSerializer(admin_A_Encontrar)
            data_usuario=usuario.objects.filter(cedula=admin_A_Encontrar_serializer.data['cedula']).values().first()
            return JsonResponse({
                'admin':admin_A_Encontrar_serializer.data['cedula'],
                'data':data_usuario
                })

    except personalAdministrativo.DoesNotExist:
        try:
            admin_A_Encontrar = personalAdministrativo.objects.get(idPersonal=cedula_Admin_or_id)
            if request.method == 'GET':
                admin_A_Encontrar_serializer = PersonalAdministrativoSerializer(admin_A_Encontrar)
                data_usuario=usuario.objects.filter(cedula=admin_A_Encontrar_serializer.data['cedula']).values().first()
                return JsonResponse({
                    'admin':admin_A_Encontrar_serializer.data['cedula'],
                    'data':data_usuario
                    })
        
        except personalAdministrativo.DoesNotExist:
            return JsonResponse({'message': 'El administador no existe'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def obtenerTodosAdministradores(request):
    try: 
        cedulas = list(personalAdministrativo.objects.all().values_list('cedula',flat=True))
        print(cedulas)
        if request.method == 'GET':
            data=usuario.objects.filter(cedula__in=cedulas).values()

            return JsonResponse({
                'data':list(data),
                
            }, safe=False)

    except cliente.DoesNotExist:
        return JsonResponse({'message': 'El administador no existe'}, status=status.HTTP_404_NOT_FOUND)

#API para obtener un cliente de la tabla de clientes a partir de la cédula
@api_view(['GET'])
def obtenerAdministrador_especifico(request, cedula_Admin):

    try: 
        admin_A_Encontrar = personalAdministrativo.objects.get(cedula=cedula_Admin)

        if request.method == 'GET':
            admin_A_Encontrar_serializer = PersonalAdministrativoSerializer(admin_A_Encontrar)
            return JsonResponse(admin_A_Encontrar_serializer.data)

    except cliente.DoesNotExist:
        return JsonResponse({'message': 'El administador no existe'}, status=status.HTTP_404_NOT_FOUND)

# ---------------------------------------------------------- Fin --------------------------------------------------

#--------------------------------------------- API's para personal operativo -------------------------------------------------
#API para luego de registrar personal operativo
@api_view(['GET', 'POST'])
@csrf_exempt
def personalOpRegistro(request):
    context = {}
    if request.method == 'POST':
        personalOp_A_Registrar_Data = JSONParser().parse(request)
        personalOp_A_Registrar_Serializer = PersonalOperativoSerializer(data=personalOp_A_Registrar_Data )
        if personalOp_A_Registrar_Serializer.is_valid():
            personalOp_A_Registrar_Serializer.save()
            return JsonResponse(personalOp_A_Registrar_Serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(personalOp_A_Registrar_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#API para obtener todo el personal operativo
@api_view(['GET'])
@csrf_exempt
def obtenerTodoPersonalOperativo(request):
    if request.method == 'GET':
        personalOp = personalOperativo.objects.all()

        cedula = request.GET.get('numCedula', None)
        if cedula is not None:
            personalOp = personalOp.filter(cedula_icontains=cedula)

        personalOp_serializer = PersonalOperativoSerializer(personalOp, many=True)
        return JsonResponse(personalOp_serializer.data, safe=False)

@api_view(['DELETE'])
@csrf_exempt
def eliminarPersonalOperativo(request, cedula_PersonalOp):
    try:
        personalOp = personalOperativo.objects.get(numCedula=cedula_PersonalOp)

        if request.method == 'DELETE':
            personalOp.delete()
            return JsonResponse({'message': 'El personal operativo ha sido eliminado exitosamente'}, status=status.HTTP_204_NO_CONTENT)

    except personalOperativo.DoesNotExist:
        return JsonResponse({'message': 'El personal operativo no existe'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@csrf_exempt
def obtener_personalop_especifico(request, cedula_PersonalOp):
    try:
        personalOp = personalOperativo.objects.get(numCedula=cedula_PersonalOp)

        if request.method == 'GET':
            personalOp_serializer = PersonalOperativoSerializer(personalOp)
            return JsonResponse(personalOp_serializer.data)
        
    except personalOperativo.DoesNotExist:
        return JsonResponse({'message': 'El personal operativo no existe'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@csrf_exempt
def verificar_personal_op(request, correo):
    try:
        personalOp = personalOperativo.objects.get(correo=correo)

        if request.method == 'GET':
            personalOp_serializer = PersonalOperativoSerializer(personalOp)
            return JsonResponse(personalOp_serializer.data)
        
    except personalOperativo.DoesNotExist:
        return JsonResponse({'message': 'El personal operativo no existe'}, status=status.HTTP_404_NOT_FOUND)



@api_view(['PUT'])
@csrf_exempt
def actualizar_personalop(request, cedula_PersonalOp):
    try:
        personalOp = personalOperativo.objects.get(numCedula=cedula_PersonalOp)

        if request.method == 'PUT':
            personalOp_data = JSONParser().parse(request)
            personalOp_serializer = PersonalOperativoSerializer(personalOp, data=personalOp_data)
            if personalOp_serializer.is_valid():
                personalOp_serializer.save()
                return JsonResponse(personalOp_serializer.data)
            return JsonResponse(personalOp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    except personalOperativo.DoesNotExist:
        return JsonResponse({'message': 'El personal operativo no existe'}, status=status.HTTP_404_NOT_FOUND)

# ---------------------------------------------------------- Fin --------------------------------------------------

#--------------------------------------------- API's para servicio -------------------------------------------------

#API para crear un servicio
@api_view(['GET', 'POST'])
@csrf_exempt
def crearServicio(request):
    if request.method == 'POST':
        servicio_Nuevo = JSONParser().parse(request)
        servicio_Nuevo_Serializer = ServicioSerializer(data = servicio_Nuevo)
        if servicio_Nuevo_Serializer.is_valid():
            servicio_Nuevo_Serializer.save()
            return JsonResponse(servicio_Nuevo_Serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(servicio_Nuevo_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#API para actualizar la información de un servicio
@api_view(['PUT', 'DELETE', 'GET'])
@csrf_exempt
def servicio_seleccionar_actualizar_eliminar(request, nombre_Servicio):
    try:
        servicio_A_Encontrar = servicio.objects.get(nombreServicio = nombre_Servicio)

        if request.method == 'PUT':
            servicio_A_Encontrar_data = JSONParser().parse(request)
            servicio_A_Encontrar_serializer = ServicioSerializer(servicio_A_Encontrar, data=servicio_A_Encontrar_data)
            if servicio_A_Encontrar_serializer.is_valid():
                servicio_A_Encontrar_serializer.save()
                return JsonResponse(servicio_A_Encontrar_serializer.data)
            return JsonResponse(servicio_A_Encontrar_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'GET':
            servicio_A_Encontrar_serializer = ServicioSerializer(servicio_A_Encontrar)
            return JsonResponse(servicio_A_Encontrar_serializer.data)
        elif request.method == 'DELETE':
            servicio_A_Encontrar.delete()
            return JsonResponse({'mensaje': 'El servicio fue eliminado exitosamente'}, status=status.HTTP_204_NO_CONTENT)


    except servicio.DoesNotExist:
        return JsonResponse({'message' : 'El servicio no existe'}, status=status.HTTP_404_NOT_FOUND)

#API VIEW para obtener los servicios creados por los administradores
@api_view(['GET', 'POST'])
@csrf_exempt
def obtenerServicio(request):
    if request.method == 'GET':
        servicios = servicio.objects.all()

        nombre_Servicio = request.GET.get('nombreServicio', None)
        if nombre_Servicio is not None:
            servicios = servicios.filter(nombre_Servicio_icontains=nombre_Servicio)

        servicios_serializer = ServicioSerializer(servicios, many=True)
        return JsonResponse(servicios_serializer.data, safe=False)

#Api para obtener los tipos de servicios y presentarlos como opcion al momento de crear un nuevo servicio
@api_view(['GET', 'POST', 'DELETE'])
def obtenerTiposServicios(request):
    if request.method == 'GET':
        tipo_servicio =  tipoServicio.objects.all()

        tarifa = request.GET.get('tarifa', None)
        if tarifa is not None:
            tipo_servicio = tipo_servicio.filter(tarifa_icontains=tarifa)

        tipo_servicio_serializer = TipoServicioSerializer(tipo_servicio, many=True)
        return JsonResponse(tipo_servicio_serializer.data, safe=False)

#API VIEW para obtener todas y enviar solicitud de servicio creado por el cliente
@api_view(['GET', 'POST'])
@csrf_exempt
def solicitarServicio(request):
    if request.method == 'POST':
        solicitud_De_Servicio = JSONParser().parse(request)
        solicitud_De_Servicio_Serializer = PedidoSerializer(data = solicitud_De_Servicio)
        if solicitud_De_Servicio_Serializer.is_valid():
            solicitud_De_Servicio_Serializer.save()
            return JsonResponse(solicitud_De_Servicio_Serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(solicitud_De_Servicio_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        solicitud_Servicio = pedido.objects.all()

        id_Pedido = request.GET.get('idPedido', None)
        if id_Pedido is not None:
            solicitud_Servicio = solicitud_Servicio.filter(id_Pedido_icontains=id_Pedido)

        solicitud_Servicio_serializer = PedidoSerializer(solicitud_Servicio, many=True)
        return JsonResponse(solicitud_Servicio_serializer.data, safe=False)

#Api para actualizar pedido de servicio por parte del administrador
@api_view(['PUT'])
@csrf_exempt
def actualizar_pedido_servicio(request, id_pedido):
    try:
        pedido_A_Encontrar = pedido.objects.get(idPedido = id_pedido)

        if request.method == 'PUT':
            pedido_A_Encontrar_data = JSONParser().parse(request)
            pedido_A_Encontrar_serializer = PedidoSerializer(pedido_A_Encontrar, data=pedido_A_Encontrar_data)
            if pedido_A_Encontrar_serializer.is_valid():
                pedido_A_Encontrar_serializer.save()
                return JsonResponse(pedido_A_Encontrar_serializer.data)
            return JsonResponse(pedido_A_Encontrar_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except servicio.DoesNotExist:
        return JsonResponse({'message' : 'El pedido no existe'}, status=status.HTTP_404_NOT_FOUND)
        
@api_view(['GET'])
@csrf_exempt
def solicitarServicioPorUsuario(request,id_cliente):
    if request.method == 'GET':
        solicitud_Servicio = pedido.objects.filter(cliente_solicitante=id_cliente)

        id_Pedido = request.GET.get('idPedido', None)
        if id_Pedido is not None:
            solicitud_Servicio = solicitud_Servicio.filter(id_Pedido_icontains=id_Pedido)

        solicitud_Servicio_serializer = PedidoSerializer(solicitud_Servicio, many=True)

        return JsonResponse(solicitud_Servicio_serializer.data, safe=False)

@api_view(['GET'])
@csrf_exempt
def solicitarIDEstadoServicio(request,nombre_servicio):
    if request.method == 'GET':
        id_estado = estadoPedido.objects.filter(estado=nombre_servicio).values().first()
        
        #id_Pedido = request.GET.get('idPedido', None)
        if (id_estado):
            #solicitud_Servicio_serializer = PedidoSerializer(solicitud_Servicio, many=True)
            return JsonResponse({'data':id_estado,'status':status.HTTP_200_OK}, safe=False)
        else:
            return JsonResponse({'mensaje':'no encontrado','status':status.HTTP_400_BAD_REQUEST})


@api_view(['GET'])
@csrf_exempt
def obtener_personal_porId(request,id):
    try:
        personalOp = personalOperativo.objects.get(idPersonal=id)

        if request.method == 'GET':
            personalOp_serializer = PersonalOperativoSerializer(personalOp)
            return JsonResponse(personalOp_serializer.data)
        
    except personalOperativo.DoesNotExist:
        return JsonResponse({'message': 'El personal operativo no existe'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@csrf_exempt
def solicitarPedidoAsigados(request,cedula):
        if request.method == 'GET':
            try:
                personalOp = personalOperativo.objects.get(numCedula=cedula)
                personalOp_serializer = PersonalOperativoSerializer(personalOp)
                solicitud_Servicio = pedido.objects.filter(personal_Encargado=personalOp_serializer.data['idPersonal'])
                print(personalOp.idPersonal)
                print(personalOp_serializer.data['idPersonal'])
                
                id_Pedido = request.GET.get('idPedido', None)
                if id_Pedido is not None:
                    solicitud_Servicio = solicitud_Servicio.filter(id_Pedido_icontains=id_Pedido)

                solicitud_Servicio_serializer = PedidoSerializer(solicitud_Servicio, many=True)

                    
                return JsonResponse({
                    'empleado':personalOp_serializer.data,
                    'pedido':solicitud_Servicio_serializer.data
                })

            except personalOperativo.DoesNotExist:
                return JsonResponse({'message' : 'El empleado no existe'}, status=status.HTTP_404_NOT_FOUND)         
            #COMPLETAR METODO PARA TRAER PEDIDOS DE EMPLEADO ASIGNADO


# -------------------------------------------- Fin ------------------------------------------------------------



#API para luego de registrar usuario, tambien registrar cliente
@api_view(['GET', 'POST'])
@csrf_exempt
def clienteRegistro(request):
    if request.method == 'POST':
        cliente_A_Registrar_Data = JSONParser().parse(request)
        cliente_A_Registrar_Serializer = ClienteSerializer(data=cliente_A_Registrar_Data )
        if cliente_A_Registrar_Serializer.is_valid():
            cliente_A_Registrar_Serializer.save()
            return JsonResponse(cliente_A_Registrar_Serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(cliente_A_Registrar_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#API para obtener un cliente de la tabla de clientes a partir de la cédula
@api_view(['GET'])
def obtenerCliente(request, cedula_Cliente):

    try: 
        cliente_A_Encontrar = cliente.objects.get(cedula=cedula_Cliente)

        if request.method == 'GET':
            cliente_A_Encontrar_serializer = ClienteSerializer(cliente_A_Encontrar)
            return JsonResponse(cliente_A_Encontrar_serializer.data)

    except cliente.DoesNotExist:
        return JsonResponse({'message': 'El cliente no existe'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def obtener_cliente_porId(request,id):
    try: 
        cliente_A_Encontrar = cliente.objects.get(idCliente=id)

        if request.method == 'GET':
            cliente_A_Encontrar_serializer = ClienteSerializer(cliente_A_Encontrar)
            data_cliente=usuario.objects.filter(cedula=cliente_A_Encontrar_serializer.data['cedula']).first()
            usuarios_serializer = UsuarioSerializer(data_cliente)
            return JsonResponse({
                'cliente':cliente_A_Encontrar_serializer.data,
                'data_cliente':usuarios_serializer.data
            })

    except cliente.DoesNotExist:
        return JsonResponse({'message': 'El cliente no existe'}, status=status.HTTP_404_NOT_FOUND)


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

#Funcion para obtener cliente de tabla clientes
@api_view(['GET'])
@csrf_exempt
def obtener_cliente_tabla_cliente(request, id_cliente):

    try: 
        cliente_A_Encontrar = cliente.objects.get(idCliente=id_cliente)

        if request.method == 'GET':
            cliente_A_Encontrar_serializer = ClienteSerializer(cliente_A_Encontrar)
            return JsonResponse(cliente_A_Encontrar_serializer.data)
        
    except cliente.DoesNotExist:
        return JsonResponse({'message:': 'El cliente no existe'}, status= status.HTTP_404_NOT_FOUND)

#Funcion para obtener datos de cliente de la tabla de usuario
@api_view(['GET'])
@csrf_exempt
def obtener_cliente_tabla_usuario(request, cedula_cliente):

    try:
        usuario_A_Encontrar = usuario.objects.get(cedula=cedula_cliente)

        if request.method == 'GET':
            usuario_A_Encontrar_serializer = UsuarioSerializer(usuario_A_Encontrar)
            return JsonResponse(usuario_A_Encontrar_serializer.data)
    
    except usuario.DoesNotExist:
        return JsonResponse({'message': 'El usuario no existe'}, status= status.HTTP_404_NOT_FOUND)




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
            request.session["USER_LOGGED"] = usuarioAEncontrar_serializer.data
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


@api_view(['GET','POST'])
@csrf_exempt
def crearPersonal(request):
    if request.method == 'POST':
        personalRegistrar_Data = JSONParser().parse(request)
        personalRegistrar_Serializer = PersonalOperativoSerializer(data = personalRegistrar_Data)
        if personalRegistrar_Serializer.is_valid():
            personalRegistrar_Serializer.save()
            return JsonResponse(personalRegistrar_Serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(personalRegistrar_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        personalOp = personalOperativo.objects.all()
        
        nombre = request.GET.get('nombres', None)
        if nombre is not None:
            personalOp = personalOp.filter(nombre_icontains=nombre)
        personalOp_serializer = PersonalOperativoSerializer(personalOp, many=True)
        return JsonResponse(personalOp_serializer.data, safe=False)

@api_view(['GET'])
@csrf_exempt
def obtenerPersonal(request):
    if request.method == 'GET':
        _personalOp = list(personalOperativo.objects.values())
        serializer = PersonalOperativoSerializer(_personalOp, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@csrf_exempt
def agregarPersonal(request):
    if request.method == 'GET':
        _personalOp = list(personalOperativo.objects.values())
        serializer = PersonalOperativoSerializer(_personalOp, many=True)
        return JsonResponse(serializer.data, safe=False)

#Para el personal Operativo
@api_view(['GET','POST','PUT','DELETE'])
@csrf_exempt
def personalApi(request,id=0):
    '''
    #registrar un nuevo usuario
    if request.method == 'POST':
        
    elif request.method == 'GET':
        usuarios = usuario.objects.all()
        
        nombre = request.GET.get('nombres', None)
        if nombre is not None:
            usuarios = usuarios.filter(nombre_icontains=nombre)
        usuarios_serializer = UsuarioSerializer(usuarios, many=True)
        return JsonResponse(usuarios_serializer.data, safe=False)

    '''
    if request.method=='GET':
        _personalOp = list(personalOperativo.objects.values())
        serializer = PersonalOperativoSerializer(_personalOp, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method=='POST':
        personalARegistrar_Data = JSONParser().parse(request)
        personalOpARegistrar_Serializer = PersonalOperativoSerializer(data = personalARegistrar_Data)
        if personalOpARegistrar_Serializer.is_valid():
            personalOpARegistrar_Serializer.save()
            return JsonResponse(personalOpARegistrar_Serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(personalOpARegistrar_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    elif request.method=='PUT':
        personalOp_data = json.loads(request.body)
        _personalOp = list(personalOperativo.filter(id=id).objects.values())
        serializer=PersonalOperativoSerializer(employee,data=personalOp_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        _personalOp = list(personalOperativo.objectsfilter(id=id).values())
        if len(_personalOp) > 0:
            personalOperativo.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Company not found..."}
        return JsonResponse("Deleted Succeffully!!", safe=False)

#inventario Vehiculo
@api_view(['GET','POST','DELETE'])
@csrf_exempt
def obtenerVehiculo(request):
    if request.method == 'GET':
        _vehiculos = list(vehiculo.objects.values())
        serializer = vehiculosMostrarSerializer(_vehiculos, many=True) 
        return JsonResponse(serializer.data, safe=False)

    elif request.method=='POST':
        vehiculoARegistrar_Data = JSONParser().parse(request)
        _vehiculos = vehiculosSerializer(data = vehiculoARegistrar_Data)
        if _vehiculos.is_valid():
            _vehiculos.save()
            return JsonResponse(_vehiculos.data, status=status.HTTP_201_CREATED)
        return JsonResponse(_vehiculos.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@csrf_exempt
def vehiculoEspecifico(request,placa):
    try:
        usuarioAppMobil = vehiculo.objects.get(placa=placa)
        if request.method == 'DELETE':
            _vehiculos = list(vehiculo.objectsfilter(placa=placa).values())
            if len(_vehiculos) > 0:
                vehiculo.objects.filter(placa=placa).delete()
                datos = {'message': "Success"}
            else:
                datos = {'message': "Company not found..."}
            return JsonResponse("Deleted Succeffully!!", safe=False)
    except vehiculo.DoesNotExist:
        return JsonResponse({'message' : 'El vehiculo no existe'}, status=status.HTTP_404_NOT_FOUND)


#inventario candado
@api_view(['GET','POST','DELETE'])
@csrf_exempt
def obtenerCandado(request):
    if request.method == 'GET':
        _candados = list(candado.objects.values())
        serializer = candadosMostrarSerializer(_candados, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method=='POST':
            candadoARegistrar_Data = JSONParser().parse(request)
            _candados = candadosSerializer(data = candadoARegistrar_Data)
            if _candados.is_valid():
                _candados.save()
                return JsonResponse(_candados.data, status=status.HTTP_201_CREATED)
            return JsonResponse(_candados.errors, status=status.HTTP_400_BAD_REQUEST)


#inventario armamento
@api_view(['GET','POST'])
@csrf_exempt
def obtenerArmamento(request):
    if request.method == 'GET':
        _armamentos = list(armamento.objects.values())
        serializer = armamentosMostrarSerializer(_armamentos, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method=='POST':
            armamentoARegistrar_Data = JSONParser().parse(request)
            _armamentos = armamentosSerializer(data = armamentoARegistrar_Data)
            if _armamentos.is_valid():
                _armamentos.save()
                return JsonResponse(_armamentos.data, status=status.HTTP_201_CREATED)
            return JsonResponse(_armamentos.errors, status=status.HTTP_400_BAD_REQUEST)


#inventario mobil
@api_view(['GET'])
@csrf_exempt
def obtenerMobil(request):
    if request.method == 'GET':
        _mobil = list(mobil.objects.values())
        serializer = MobilSerializer(_mobil, many=True)
        return JsonResponse(serializer.data, safe=False)


def mobilRegistro(request):
    #registrar un nuevo usuario

    if request.method == 'GET':
        mobils = mobil.objects.all()
        
        numeroCell = request.GET.get('numeroCell', None)
        if numeroCell is not None:
            mobils = mobils.filter(numeroCell_icontains=numeroCell)
        mobils_serializer = MobilSerializer(mobils, many=True)
        return JsonResponse(mobils_serializer.data, safe=False)


        
#Función para obtener datos de un usuario para validacion en inicio sesion
@api_view(['GET', 'PUT'])
@csrf_exempt
def mobilInicioSesion(request, UsuarioApp):

    try:
        usuarioAppMobil = mobil.objects.get(usuarioApp=UsuarioApp)

        #mandar datos para validación
        if request.method == 'GET':
            usuarioAppMobil_serializer = MobilSerializer(usuarioAppMobil) #El del final es el modelo
            request.session["USER_LOGGED"] = usuarioAppMobil_serializer.data
            return JsonResponse(usuarioAppMobil_serializer.data)
            
        elif request.method == 'PUT':
            usuarioAppMobil_data = JSONParser().parse(request)
            usuarioAppMobil_serializer = MobilSerializer(usuarioAppMobil, data=usuarioAppMobil_data)
            if usuarioAppMobil_serializer.is_valid():
                usuarioAppMobil_serializer.save()


                return JsonResponse(usuarioAppMobil_serializer.data)
                
            return JsonResponse(usuarioAppMobil_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except usuario.DoesNotExist:
        return JsonResponse({'message' : 'El usuario no existe'}, status=status.HTTP_404_NOT_FOUND)


#Api para obtener Sucursales y presentarlas en el registro de un administrador
@api_view(['GET', 'POST', 'DELETE'])
def obtenerSucursal(request):
    if request.method == 'GET':
        sucursales = sucursal.objects.all()

        direccion = request.GET.get('direccion', None)
        if direccion is not None:
            sucursales = sucursales.filter(direccion_icontains=direccion)

        sucursales_serializer = SucursalSerializer(sucursales, many=True)
        return JsonResponse(sucursales_serializer.data, safe=False)
