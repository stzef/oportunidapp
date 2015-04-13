# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habilidades', '0002_auto_20150413_1313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habilidadesmodel',
            old_name='id_usuario',
            new_name='usuario',
        ),
    ]
