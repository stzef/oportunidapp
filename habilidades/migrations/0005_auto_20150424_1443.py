# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime

class Migration(migrations.Migration):

    dependencies = [
        ('habilidades', '0004_habilidadesmodel_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='habilidadesmodel',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.date.today(), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='habilidadesmodel',
            name='foto',
            field=models.ImageField(null=True, upload_to=b'habilidades/img/', blank=True),
        ),
    ]
