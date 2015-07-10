# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('necesito', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenecesitomodel',
            name='usuarioRequerido',
            field=models.ForeignKey(related_name=b'requerido', to='usuarios.perfilUsuarioModel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tenecesitomodel',
            name='usuarioSolicitante',
            field=models.ForeignKey(related_name=b'solicitante', to='usuarios.perfilUsuarioModel'),
            preserve_default=True,
        ),
    ]
