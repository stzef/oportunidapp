# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20150330_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilusuariomodel',
            name='fnacimiento',
            field=models.DateField(null=True, blank=True),
        ),
    ]
