# Generated by Django 3.2.16 on 2023-01-24 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_alter_personaloperativo_cargo_trabajo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaloperativo',
            name='cargo_trabajo',
            field=models.CharField(max_length=1000),
        ),
    ]
