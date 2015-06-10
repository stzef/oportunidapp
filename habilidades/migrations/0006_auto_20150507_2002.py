# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habilidades', '0005_auto_20150424_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='habilidadesmodel',
            name='slug',
            field=models.CharField(default=b'', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='habilidadesmodel',
            name='foto',
            field=models.ImageField(default=b'habilidades/img/no_image.png', null=True, upload_to=b'habilidades/img/', blank=True),
        ),
        migrations.AlterField(
            model_name='habilidadesmodel',
            name='num_solicitudes',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='habilidadesmodel',
            name='val_promedio',
            field=models.IntegerField(default=4, null=True, blank=True),
        ),
    ]
