# Generated by Django 3.2.16 on 2023-01-08 05:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Canal',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tiempo', models.DateTimeField(auto_now_add=True)),
                ('actualizar', models.DateTimeField(auto_now=True)),
                ('servicio', models.CharField(choices=[('Custodia', 'Custodia Armada'), ('Transporte', 'Transporte de productos'), ('Chofer', 'Chofer seguro'), ('Guardia', 'Guardia de seguridad')], max_length=23)),
                ('id_servicio', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CanalUsuario',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tiempo', models.DateTimeField(auto_now_add=True)),
                ('actualizar', models.DateTimeField(auto_now=True)),
                ('canal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.canal')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.usuario')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CanalMensaje',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tiempo', models.DateTimeField(auto_now_add=True)),
                ('actualizar', models.DateTimeField(auto_now=True)),
                ('texto', models.TextField()),
                ('canal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.canal')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.usuario')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='canal',
            name='usuarios',
            field=models.ManyToManyField(blank=True, through='chat.CanalUsuario', to='empresa.usuario'),
        ),
    ]
