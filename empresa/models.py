from django.conf import settings
from django.db import models
from django.utils import timezone


class sucursal(models.Model):
    idSucursal = models.IntegerField(primary_key=True)
    direccion = models.CharField(max_length=80)

class rol(models.Model):
    idRol = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=150)

    def __str__(self):
        return str(self.tipo)

class usuario(models.Model):
    sexo_CHOICES=(("M","masculino"),("F","femenino"))
    cedula = models.CharField(max_length=10, primary_key=True)
    apellidos = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    fechaNac = models.DateField()
    sexo = models.CharField(max_length=30,choices=sexo_CHOICES)
    direccion = models.EmailField()
    telefono = models.CharField(max_length=10)
    correo = models.EmailField(max_length=70, unique=True)
    contrasenia = models.CharField(max_length=15)
    fechaRegistro = models.DateTimeField(auto_now=False, auto_now_add=True)
    tokenMovil=models.CharField(max_length=200)
    rol = models.ForeignKey(rol, on_delete=models.CASCADE)
    
    def __str__(self):
         return self.nombres+" "+ self.apellidos

class estado(models.Model):
    idEstado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=30)

class estadoPedido(models.Model):
    estadoPe_CHOICES = (("En Espera","En Espera"),("En Curso","En Curso"),("Finalizado","Finalizado"),("Cancelado","Cancelado"))
    idEstadoP = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=20,choices=estadoPe_CHOICES)

class cargo(models.Model):
    tipoCargo_CHOICES=(("Ad","administrativo"),("Op","operativo"))
    idCargo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=150)
    tipo = models.CharField(max_length=30,choices=tipoCargo_CHOICES)

class personalAdministrativo(models.Model):
    idPersonal = models.AutoField(primary_key=True)
    inicioOperanciones = models.DateField(auto_now=False, auto_now_add=True)
    finOpeaciones = models.DateField(auto_now=False, auto_now_add=True,blank=True)
    sucursal = models.ForeignKey(sucursal, on_delete=models.CASCADE)
    cedula = models.ForeignKey(usuario, on_delete=models.CASCADE)
    cargo = models.ForeignKey(cargo, on_delete=models.CASCADE)
    estado = models.ForeignKey(estado, on_delete=models.CASCADE)
    fechaModificacion = models.DateField(auto_now=True, auto_now_add=False)
    #archivosAd = models.

class publicidad(models.Model):
    idPublicidad = models.AutoField(primary_key=True)
    autor = models.ForeignKey(personalAdministrativo, on_delete=models.CASCADE)
    nombreCliente = models.CharField(max_length=50)
    correoCliente = models.CharField(max_length=50)
    numeroTelf = models.CharField(max_length=50)
    fechaInicioPubli = models.DateField(auto_now=False, auto_now_add=True)
    fechaFinPubli = models.DateField(auto_now=False, auto_now_add=True)
    costo = models.FloatField(default=0)

class cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    cedula = models.ForeignKey(usuario, on_delete=models.CASCADE)

class metodoPago(models.Model):
    idTipo = models.AutoField(primary_key=True)
    metodo = models.CharField(max_length=20)

class tarjeta(models.Model):
    tipoTarjeta_CHOICES = (("debito","debito"),("credito","credito"))
    numTarjeta = models.CharField(max_length=16)
    banco = models.CharField(max_length=50)
    tipo = models.CharField(max_length=10,choices=tipoTarjeta_CHOICES)
    propietario = models.ForeignKey(cliente, on_delete=models.CASCADE)

    #agregadoPor = models.ForeignKey(personalAdministrativo, on_delete=models.CASCADE)

class personalOperativo(models.Model):
    sexo_CHOICES=(("M","masculino"),("F","femenino"))
    idPersonal = models.AutoField(primary_key=True)
    numCedula = models.CharField(max_length=10, unique=True)
    apellidos = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    fechaNac = models.DateField()
    sexo = models.CharField(max_length=30,choices=sexo_CHOICES)
    direccion = models.EmailField()
    telefono = models.CharField(max_length=10)
    correo = models.EmailField(max_length=70, unique=True)
    fechaRegistro = models.DateTimeField(auto_now=False, auto_now_add=True)
    sucursal = models.ForeignKey(sucursal, on_delete=models.CASCADE)
    estado = models.ForeignKey(estado, on_delete=models.CASCADE)
    fotoOp = models.ImageField(upload_to='uploads/')


class tipoServicio(models.Model):
    idTipo = models.AutoField(primary_key=True)
    tarifa = models.FloatField(default=0)

class servicio(models.Model):
    idServicio = models.AutoField(primary_key=True)
    nombreServicio = models.CharField(max_length=50)
    costo = models.FloatField()
    detalles = models.CharField(max_length=100)
    fecha_Creacion = models.DateTimeField()
    tipo_Servicio = models.ForeignKey(tipoServicio, on_delete=models.CASCADE)
    administrador_Creador = models.ForeignKey(personalAdministrativo, on_delete=models.CASCADE)
    incluir_Vehiculo = models.BooleanField()


class pedido(models.Model):
    idPedido = models.AutoField(primary_key=True)
    nombre_Servicio = models.CharField(max_length=50)
    costo = models.FloatField()
    fecha_Solicitud = models.DateTimeField()
    fecha_Inicio = models.DateField()
    fecha_Finalizacion = models.DateField()
    hora_Inicio = models.TimeField()
    hora_Finalizacion = models.TimeField()
    latitud_Origen = models.DecimalField(max_digits=22, decimal_places=18)
    longitud_Origen = models.DecimalField(max_digits=22, decimal_places=18)
    latitud_Destino = models.DecimalField(max_digits=22, decimal_places=18)
    longitud_Destino = models.DecimalField(max_digits=22, decimal_places=18)
    cantidad_Empleados_Asignados = models.IntegerField()
    cantidad_vehiculos = models.IntegerField()
    detalle = models.CharField(max_length=300)
    estado = models.ForeignKey(estadoPedido, on_delete=models.CASCADE)
    metodo_Pago = models.ForeignKey(metodoPago, on_delete=models.CASCADE)
    idServicio = models.ForeignKey(servicio, on_delete=models.CASCADE)
    administrador_Encargado = models.ForeignKey(personalAdministrativo, on_delete=models.CASCADE)
    cliente_solicitante = models.ForeignKey(cliente, on_delete=models.CASCADE)
    

class detallePersonalAsignado(models.Model):
    idPersonalAsignado = models.AutoField(primary_key=True)
    encargado_Servicio = models.BooleanField()
    cargo = models.CharField(max_length=30)
    idPedido = models.ForeignKey(pedido, on_delete=models.CASCADE)
    idEmpleado = models.ForeignKey(personalOperativo, on_delete=models.CASCADE)


class equipamiento(models.Model):
    idEquipo = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=20)
    sucursal = models.ForeignKey(sucursal, on_delete=models.CASCADE)

class detallePedido(models.Model):
    idPedido = models.ForeignKey(pedido, on_delete=models.CASCADE)
    idequipamiento = models.ForeignKey(equipamiento, on_delete=models.CASCADE)

class detalleServicio(models.Model):
    idServicio =  models.ForeignKey(servicio, on_delete=models.CASCADE)
    idEquipamiento = models.ForeignKey(equipamiento, on_delete=models.CASCADE)


class mobil(models.Model):
    numeroCell = models.CharField(max_length=10,primary_key=True)
    idEquipamiento = models.ForeignKey(equipamiento, on_delete=models.CASCADE)
    marca = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    #fechaIngreso = models.DateField(auto_now=False, auto_now_add=True)
    #fechaCeseOperaciones = models.DateField(auto_now=False)
    usuarioApp = models.CharField(max_length=25)
    contrasenia = models.CharField(max_length=15)

class vehiculo(models.Model):
    placa = models.CharField(max_length=10,primary_key=True)
    idEquipamiento = models.ForeignKey(equipamiento, on_delete=models.CASCADE)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    anio = models.IntegerField()
    #fechaIngreso = models.DateField(auto_now=False, auto_now_add=True)
    #fechaCeseOperaciones = models.DateField(auto_now=False)

class candado(models.Model):
    numSerie = models.CharField(max_length=20,primary_key=True)
    idEquipamiento = models.ForeignKey(equipamiento, on_delete=models.CASCADE)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    anio = models.IntegerField()
    #fechaIngreso = models.DateField(auto_now=False, auto_now_add=True)
    #fechaCeseOperaciones = models.DateField(auto_now=False)
'''
class municion(models.Model):
    idMunicion = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=20)
    cantidad = models.IntegerField()
    calibre = models.FloatField(default=0)
'''

class armamento(models.Model):
    numSerie = models.CharField(max_length=20,primary_key=True)
    idEquipamiento = models.ForeignKey(equipamiento, on_delete=models.CASCADE)
    marca = models.CharField(max_length=20)
    clase = models.CharField(max_length=20)
    #municion = models.ForeignKey(municion, on_delete=models.CASCADE)
    #fechaIngreso = models.DateField(auto_now=False, auto_now_add=True)
    #fechaCeseOperaciones = models.DateField(auto_now=False)

class detallePerfilOp(models.Model):
    idDetallePerfil = models.AutoField(primary_key=True)
    cargo = models.ForeignKey(cargo, on_delete=models.CASCADE)
    idPersonalOp = models.ForeignKey(personalOperativo, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20)










