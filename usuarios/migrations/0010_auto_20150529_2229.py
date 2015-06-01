# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_perfilusuariomodel_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilusuariomodel',
            name='foto',
            field=models.ImageField(default=b'habilidades/img/no_image.png', null=True, upload_to=b'usuarios/avatar/', blank=True),
        ),
    ]
