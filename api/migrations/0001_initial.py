# Generated by Django 4.0.4 on 2022-05-19 06:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('rut', models.CharField(max_length=9)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=12)),
                ('direccion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(choices=[('Instrumento de cuerda', (('guitarras', 'Guitarras'), ('bajos', 'Bajos'), ('pianos', 'Pianos'))), ('Percusion', (('baterias_acusticas', 'Baterias Acusticas'), ('bateria_electronica', 'Bateria Electronica'))), ('Amplificadores', (('cabezales', 'Cabezales'), ('cajas', 'Cajas'))), ('Accesorios_varios', 'Accesorios varios')], max_length=25)),
                ('marca', models.CharField(max_length=30)),
                ('codigo', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=35)),
                ('valor', models.IntegerField()),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]