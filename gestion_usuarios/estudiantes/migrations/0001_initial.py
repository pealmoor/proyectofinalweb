# Generated by Django 5.1.3 on 2024-11-27 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo_electronico', models.EmailField(max_length=254, unique=True)),
                ('fecha_nacimiento', models.DateField()),
                ('codigo_estudiante', models.CharField(max_length=15, unique=True)),
                ('carrera', models.CharField(max_length=100)),
                ('semestre', models.PositiveSmallIntegerField()),
                ('promedio', models.FloatField(default=0.0)),
            ],
        ),
    ]
