# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habilidades', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habilidadesmodel',
            old_name='id_categoria',
            new_name='categoria',
        ),
        migrations.AlterField(
            model_name='habilidadesmodel',
            name='estado',
            field=models.CharField(default=b'1', max_length=1, choices=[(b'1', b'Activo'), (b'2', b'Inactivo'), (b'3', b'Eliminado')]),
        ),
    ]
