# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habilidades', '0007_remove_habilidadesmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habilidadesmodel',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='habilidadesmodel',
            name='val_promedio',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
