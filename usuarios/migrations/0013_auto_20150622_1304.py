# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0012_auto_20150609_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilusuariomodel',
            name='foto',
            field=models.ImageField(default=b'usuarios/avatar/user.jpg', null=True, upload_to=b'usuarios/avatar/', blank=True),
        ),
    ]
