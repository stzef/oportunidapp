# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habilidades', '0010_auto_20150616_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='habcategoriasmodel',
            name='slug',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='habilidadesmodel',
            name='slug',
            field=models.SlugField(editable=False),
        ),
    ]
