# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
