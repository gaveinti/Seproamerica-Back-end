# Generated by Django 3.2.16 on 2022-12-15 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_canalmensaje_leido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='canalmensaje',
            name='leido',
        ),
    ]
