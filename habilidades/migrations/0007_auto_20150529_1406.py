# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habilidades', '0006_auto_20150519_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habilidadesmodel',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='habilidadesmodel',
            name='foto',
            field=models.ImageField(default=b'habilidades/img/no_image.png', null=True, upload_to=b'habilidades/img', blank=True),
        ),
        migrations.AlterField(
            model_name='habilidadesmodel',
            name='val_promedio',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
