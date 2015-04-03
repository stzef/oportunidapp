# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilusuariomodel',
            name='cedula',
            field=models.IntegerField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perfilusuariomodel',
            name='fnacimiento',
            field=models.DateField(blank=True),
        ),
    ]
