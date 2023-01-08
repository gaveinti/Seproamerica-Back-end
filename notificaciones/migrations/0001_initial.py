# Generated by Django 3.2.16 on 2023-01-08 18:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenNotificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('level', models.CharField(choices=[('Success', 'success'), ('Info', 'info'), ('Wrong', 'wrong'), ('Cualquiera', 'cualquiera'), ('Nuevo Mensaje', 'nuevo mensaje'), ('Servicio solicitado', 'servicio_solicitado'), ('Servicio pagado', 'servicio_pagado'), ('Servicio cancelado', 'servicio_cancelado')], default='Cualquiera', max_length=20)),
                ('object_id_actor', models.PositiveIntegerField()),
                ('verbo', models.CharField(max_length=220)),
                ('timestamp', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('read', models.BooleanField(default=False)),
                ('publico', models.BooleanField(default=True)),
                ('eliminado', models.BooleanField(default=False)),
                ('actor_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notificar_actor', to='contenttypes.contenttype')),
                ('destiny', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones', to='empresa.usuario')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]