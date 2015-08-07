# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('muebles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mueble',
            name='descripcion',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='mueble',
            name='dimensiones',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
