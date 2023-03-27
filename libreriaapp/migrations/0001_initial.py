# Generated by Django 4.1.7 on 2023-03-26 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='libros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')),
                ('titulo', models.CharField(max_length=45)),
                ('autor', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=28)),
                ('fecha_lanzamiento', models.DateField()),
            ],
            options={
                'db_table': 'libros',
                'ordering': ['titulo'],
            },
        ),
        migrations.CreateModel(
            name='ulector',
            fields=[
                ('id_lector', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id lector')),
                ('cedula', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('telefono', models.IntegerField()),
                ('observacion', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'ulector',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')),
                ('usuario', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=50)),
                ('clave', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'usuarios',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='alquiler',
            fields=[
                ('id_alquiler', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id alquiler')),
                ('fecha_salida', models.DateField()),
                ('fecha_entrada', models.DateField()),
                ('id_libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libreriaapp.libros')),
                ('id_ulector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libreriaapp.ulector')),
            ],
            options={
                'db_table': 'alquiler',
                'ordering': ['fecha_salida'],
            },
        ),
    ]