# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habilidades', '0009_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='habilidadesmodel',
            name='slug',
            field=models.SlugField(default='default'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='habilidadesmodel',
            name='nhabilidad',
            field=models.CharField(max_length=50),
        ),
    ]
