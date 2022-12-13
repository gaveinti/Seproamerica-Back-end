# Generated by Django 3.2.16 on 2022-12-13 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cargo',
            fields=[
                ('idCargo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=150)),
                ('tipo', models.CharField(choices=[('Ad', 'administrativo'), ('Op', 'operativo')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('idCliente', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='equipamiento',
            fields=[
                ('idEquipo', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='estado',
            fields=[
                ('idEstado', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='estadoPedido',
            fields=[
                ('idEstadoP', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(choices=[('En Espera', 'En Espera'), ('En Curso', 'En Curso'), ('Finalizado', 'Finalizado'), ('Cancelado', 'Cancelado')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='metodoPago',
            fields=[
                ('idTipo', models.AutoField(primary_key=True, serialize=False)),
                ('metodo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='personalAdministrativo',
            fields=[
                ('idPersonal', models.AutoField(primary_key=True, serialize=False)),
                ('inicioOperanciones', models.DateField(auto_now_add=True)),
                ('finOpeaciones', models.DateField(auto_now_add=True)),
                ('fechaModificacion', models.DateField(auto_now=True)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.cargo')),
            ],
        ),
        migrations.CreateModel(
            name='rol',
            fields=[
                ('idRol', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='sucursal',
            fields=[
                ('idSucursal', models.IntegerField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='tipoServicio',
            fields=[
                ('idTipo', models.AutoField(primary_key=True, serialize=False)),
                ('tarifa', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='vehiculo',
            fields=[
                ('placa', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('anio', models.IntegerField()),
                ('idEquipamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.equipamiento')),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('cedula', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('apellidos', models.CharField(max_length=50)),
                ('nombres', models.CharField(max_length=50)),
                ('fechaNac', models.DateField()),
                ('sexo', models.CharField(choices=[('M', 'masculino'), ('F', 'femenino')], max_length=30)),
                ('direccion', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=10)),
                ('correo', models.EmailField(max_length=70, unique=True)),
                ('contrasenia', models.CharField(max_length=15)),
                ('fechaRegistro', models.DateTimeField(auto_now_add=True)),
                ('tokenMovil', models.CharField(max_length=200)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.rol')),
            ],
        ),
        migrations.CreateModel(
            name='tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numTarjeta', models.CharField(max_length=16)),
                ('banco', models.CharField(max_length=50)),
                ('tipo', models.CharField(choices=[('debito', 'debito'), ('credito', 'credito')], max_length=10)),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='servicio',
            fields=[
                ('idServicio', models.AutoField(primary_key=True, serialize=False)),
                ('nombreServicio', models.CharField(max_length=50)),
                ('costo', models.FloatField()),
                ('detalles', models.CharField(max_length=100)),
                ('fecha_Creacion', models.DateTimeField()),
                ('incluir_Vehiculo', models.BooleanField()),
                ('administrador_Creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.personaladministrativo')),
                ('tipo_Servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.tiposervicio')),
            ],
        ),
        migrations.CreateModel(
            name='publicidad',
            fields=[
                ('idPublicidad', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCliente', models.CharField(max_length=50)),
                ('correoCliente', models.CharField(max_length=50)),
                ('numeroTelf', models.CharField(max_length=50)),
                ('fechaInicioPubli', models.DateField(auto_now_add=True)),
                ('fechaFinPubli', models.DateField(auto_now_add=True)),
                ('costo', models.FloatField(default=0)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.personaladministrativo')),
            ],
        ),
        migrations.CreateModel(
            name='personalOperativo',
            fields=[
                ('idPersonal', models.AutoField(primary_key=True, serialize=False)),
                ('numCedula', models.CharField(max_length=10, unique=True)),
                ('apellidos', models.CharField(max_length=50)),
                ('nombres', models.CharField(max_length=50)),
                ('fechaNac', models.DateField()),
                ('sexo', models.CharField(choices=[('M', 'masculino'), ('F', 'femenino')], max_length=30)),
                ('direccion', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=10)),
                ('correo', models.EmailField(max_length=70, unique=True)),
                ('fechaRegistro', models.DateTimeField(auto_now_add=True)),
                ('fotoOp', models.ImageField(upload_to='uploads/')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.estado')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.sucursal')),
            ],
        ),
        migrations.AddField(
            model_name='personaladministrativo',
            name='cedula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.usuario'),
        ),
        migrations.AddField(
            model_name='personaladministrativo',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.estado'),
        ),
        migrations.AddField(
            model_name='personaladministrativo',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.sucursal'),
        ),
        migrations.CreateModel(
            name='pedido',
            fields=[
                ('idPedido', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_Servicio', models.CharField(max_length=50)),
                ('costo', models.FloatField()),
                ('fecha_Solicitud', models.DateTimeField()),
                ('fecha_Inicio', models.DateField()),
                ('fecha_Finalizacion', models.DateField()),
                ('hora_Inicio', models.TimeField()),
                ('hora_Finalizacion', models.TimeField()),
                ('latitud_Origen', models.DecimalField(decimal_places=18, max_digits=22)),
                ('longitud_Origen', models.DecimalField(decimal_places=18, max_digits=22)),
                ('latitud_Destino', models.DecimalField(decimal_places=18, max_digits=22)),
                ('longitud_Destino', models.DecimalField(decimal_places=18, max_digits=22)),
                ('cantidad_Empleados_Asignados', models.IntegerField()),
                ('cantidad_vehiculos', models.IntegerField()),
                ('detalle', models.CharField(max_length=300)),
                ('administrador_Encargado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.personaladministrativo')),
                ('cliente_solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.cliente')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.estadopedido')),
                ('idServicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.servicio')),
                ('metodo_Pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.metodopago')),
            ],
        ),
        migrations.CreateModel(
            name='mobil',
            fields=[
                ('numeroCell', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('usuarioApp', models.CharField(max_length=25)),
                ('contrasenia', models.CharField(max_length=15)),
                ('idEquipamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.equipamiento')),
            ],
        ),
        migrations.AddField(
            model_name='equipamiento',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.sucursal'),
        ),
        migrations.CreateModel(
            name='detalleServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idEquipamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.equipamiento')),
                ('idServicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.servicio')),
            ],
        ),
        migrations.CreateModel(
            name='detallePersonalAsignado',
            fields=[
                ('idPersonalAsignado', models.AutoField(primary_key=True, serialize=False)),
                ('encargado_Servicio', models.BooleanField()),
                ('cargo', models.CharField(max_length=30)),
                ('idEmpleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.personaloperativo')),
                ('idPedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='detallePerfilOp',
            fields=[
                ('idDetallePerfil', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=20)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.cargo')),
                ('idPersonalOp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.personaloperativo')),
            ],
        ),
        migrations.CreateModel(
            name='detallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idPedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.pedido')),
                ('idequipamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.equipamiento')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='cedula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.usuario'),
        ),
        migrations.CreateModel(
            name='candado',
            fields=[
                ('numSerie', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('anio', models.IntegerField()),
                ('idEquipamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.equipamiento')),
            ],
        ),
        migrations.CreateModel(
            name='armamento',
            fields=[
                ('numSerie', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=20)),
                ('clase', models.CharField(max_length=20)),
                ('idEquipamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.equipamiento')),
            ],
        ),
    ]
