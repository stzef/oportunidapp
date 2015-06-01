# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20150330_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilusuariomodel',
            name='foto',
            field=models.ImageField(null=True, upload_to=b'usuarios/avatar/', blank=True),
            preserve_default=True,
        ),
    ]
