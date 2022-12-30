from rest_framework import serializers 
from empresa.models import usuario 
from empresa.models import vehiculo, mobil, armamento, candado, personalOperativo, personalAdministrativo, pedido, cliente, servicio
from empresa.models import sucursal

class UsuarioSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = usuario
        fields = ('sexo_CHOICES',
                  'cedula',
                  'apellidos',
                  'nombres',
                  'fechaNac',
                  'direccion',
                  'telefono',
                  'correo',
                  'contrasenia',
                  'fechaRegistro',
                  'rol')

#Para el inventario
class vehiculosMostrarSerializer (serializers.ModelSerializer):
    class Meta:
        model = vehiculo
        fields = (
                'placa',
                'marca',
                'modelo',
                'color',
                'anio',)

#para el registro hasta poder arreglar
class vehiculosSerializer (serializers.ModelSerializer):
    class Meta:
        model = vehiculo
        fields = (
                'placa',
                'marca',
                'modelo',
                'color',
                'anio',
                'idEquipamiento')

class candadosMostrarSerializer (serializers.ModelSerializer):
    class Meta:
        model = candado
        fields = (
                'numSerie',
                'marca',
                'modelo',
                'color',
                'anio',)

class candadosSerializer (serializers.ModelSerializer):
    class Meta:
        model = candado
        fields = (
                'numSerie',
                'marca',
                'modelo',
                'color',
                'anio',
                'idEquipamiento')

class armamentosMostrarSerializer (serializers.ModelSerializer):
    class Meta:
        model = armamento
        fields = (
                'numSerie',
                'marca',
                'clase')

class armamentosSerializer (serializers.ModelSerializer):
    class Meta:
        model = armamento
        fields = (
                'numSerie',
                'marca',
                'clase',
                'idEquipamiento')

class PersonalAdministrativoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = personalAdministrativo
        fields = ('idPersonal',
                  'inicioOperanciones',
                  'finOpeaciones',
                  'sucursal',
                  'cedula',
                  'cargo',
                  'estado',
                  'fechaModificacion',
                  )

class PersonalOperativoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = personalOperativo
        fields = ('sexo_CHOICES',
                  'idPersonal',
                  'numCedula',
                  'apellidos',
                  'nombres',
                  'fechaNac',
                  'sexo',
                  'direccion',
                  'telefono',
                  'correo',
                  'fechaRegistro',
                  #'agregadoPor',
                  #'sucursal',
                  #'estado',
                  #'rol'
                  )

class MobilSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = mobil
        fields = ('numeroCell',
                  'idEquipamiento',
                  'marca',
                  'color',
                  'usuarioApp',
                  'contrasenia',
                  )

class PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = pedido
        fields = ('idPedido',
                  'nombre_Servicio',
                  'costo',
                  'fecha_Solicitud',
                  'fecha_Inicio',
                  'fecha_Finalizacion',
                  'hora_Inicio',
                  'hora_Finalizacion',
                  'latitud_Origen',
                  'longitud_Origen',
                  'latitud_Destino',
                  'longitud_Destino',
                  'cantidad_Empleados_Asignados',
                  'cantidad_vehiculos',
                  'detalle',
                  'estado',
                  'metodo_Pago',
                  'idServicio',
                  'administrador_Encargado',
                  'personal_Encargado',
                  'cliente_solicitante'
                )

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = cliente
        fields = ('idCliente',
                  'cedula'
                )

class ServicioSerializer(serializers.ModelSerializer):

    class Meta:
        model = servicio
        fields = ('idServicio',
                  'nombreServicio',
                  'costo',
                  'detalles',
                  'fecha_Creacion',
                  'tipo_Servicio',
                  'administrador_Creador',
                  'incluir_Vehiculo',
                  'icono'
                )

class SucursalSerializer(serializers.ModelSerializer):

    class Meta:
        model = sucursal
        fields = ('idSucursal',
                  'direccion'
                )