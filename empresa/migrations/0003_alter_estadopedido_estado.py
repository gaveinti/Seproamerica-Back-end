# Generated by Django 3.2.16 on 2023-01-21 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_pedido_candado_satelital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadopedido',
            name='estado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('En Proceso', 'En Proceso'), ('Finalizado', 'Finalizado'), ('Cancelado', 'Cancelado')], max_length=20),
        ),
    ]
