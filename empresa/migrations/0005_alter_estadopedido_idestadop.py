# Generated by Django 3.2.16 on 2023-01-21 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0004_alter_estadopedido_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadopedido',
            name='idEstadoP',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
