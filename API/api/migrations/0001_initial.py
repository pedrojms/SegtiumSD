# Generated by Django 3.1.4 on 2021-01-17 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruc', models.CharField(max_length=250)),
                ('nombre', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=250)),
                ('direccion', models.TextField()),
                ('representante', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('descripcion', models.TextField()),
                ('fuente', models.CharField(max_length=250)),
                ('fecha', models.DateField()),
                ('imagen', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Oficina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=250)),
                ('direccion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('descripcion', models.TextField()),
                ('preciobase', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('apellido', models.CharField(max_length=250)),
                ('correo', models.EmailField(max_length=254)),
                ('contrasena', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('totalventas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('apellido', models.CharField(max_length=250)),
                ('cedula', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=250)),
                ('correo', models.EmailField(max_length=254)),
                ('oficina_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.oficina')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.TextField()),
                ('fecha', models.DateField()),
                ('ciudad', models.CharField(max_length=250)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('precio', models.FloatField()),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.empresa')),
                ('servicio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.servicio')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
                ('vendedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='Brochure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('fecha', models.DateField()),
                ('servicio_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.servicio')),
            ],
        ),
        migrations.CreateModel(
            name='Beneficios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('descripcion', models.TextField()),
                ('servicio_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.servicio')),
            ],
        ),
    ]
