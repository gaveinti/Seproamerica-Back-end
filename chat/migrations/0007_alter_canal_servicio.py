# Generated by Django 3.2.16 on 2022-11-08 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_alter_canal_servicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canal',
            name='servicio',
            field=models.CharField(choices=[('CA', 'custodia'), ('GS', 'guardia'), ('TM', 'transportar'), ('CS', 'chofer')], max_length=20),
        ),
    ]
