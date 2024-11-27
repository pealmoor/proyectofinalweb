# Generated by Django 5.1.3 on 2024-11-27 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo_electronico', models.EmailField(max_length=254, unique=True)),
                ('direccion', models.CharField(max_length=150)),
                ('fecha_nacimiento', models.DateField()),
                ('programa', models.CharField(max_length=100)),
            ],
        ),
    ]
