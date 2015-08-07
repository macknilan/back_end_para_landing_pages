# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import muebles.models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField(max_length=240, verbose_name=b'Descripcion del mueble')),
                ('dimensiones', models.TextField(max_length=240, verbose_name=b'Dimenciones del mueble')),
                ('foto_1', models.ImageField(upload_to=muebles.models.change_file_name, max_length=50, verbose_name=b'Fotos del mueble 1')),
                ('foto_2', models.ImageField(upload_to=muebles.models.change_file_name, max_length=50, verbose_name=b'Fotos del mueble 2')),
                ('foto_3', models.ImageField(upload_to=muebles.models.change_file_name, max_length=50, verbose_name=b'Fotos del mueble 3')),
                ('foto_4', models.ImageField(upload_to=muebles.models.change_file_name, max_length=50, verbose_name=b'Fotos del mueble 4')),
                ('foto_5', models.ImageField(upload_to=muebles.models.change_file_name, max_length=50, verbose_name=b'Fotos del mueble 5')),
                ('modelo', models.CharField(max_length=40, verbose_name=b'Modelo (Nombre) ')),
                ('oferta', models.SmallIntegerField(default=0, verbose_name=b'\xc2\xbfOferta?')),
                ('precio', models.DecimalField(verbose_name=b'Precio del mueble', max_digits=10, decimal_places=2)),
                ('slug', models.CharField(unique=True, max_length=140, blank=True)),
                ('categoria', models.ForeignKey(to='categorias.Categoria')),
            ],
            bases=(muebles.models.SlugMixin, models.Model),
        ),
    ]
