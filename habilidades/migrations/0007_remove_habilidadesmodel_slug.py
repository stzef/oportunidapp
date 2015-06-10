# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habilidades', '0006_auto_20150507_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habilidadesmodel',
            name='slug',
        ),
    ]
