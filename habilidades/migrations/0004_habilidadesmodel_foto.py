# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habilidades', '0003_auto_20150413_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='habilidadesmodel',
            name='foto',
            field=models.ImageField(null=True, upload_to=b'/', blank=True),
            preserve_default=True,
        ),
    ]
