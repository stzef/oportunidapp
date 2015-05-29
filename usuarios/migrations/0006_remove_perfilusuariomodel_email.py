# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_perfilusuariomodel_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfilusuariomodel',
            name='email',
        ),
    ]
