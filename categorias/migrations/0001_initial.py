# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import categorias.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cat_mueble', models.CharField(default=b'ninguno', max_length=10, verbose_name=b'Categoria del mueble', choices=[(b'ninguno', b'Ninguno'), (b'comedores', b'Comedores'), (b'cocinas', b'Cocinas'), (b'cunas', b'Cunas'), (b'chifoniers', b'Chifoniers'), (b'recamaras', b'Recamaras')])),
                ('imagen_categoria', models.ImageField(upload_to=categorias.models.change_file_name, max_length=50, verbose_name=b'Foto de Categoria')),
                ('slug', models.CharField(unique=True, max_length=140, blank=True)),
            ],
            bases=(categorias.models.SlugMixin, models.Model),
        ),
    ]
