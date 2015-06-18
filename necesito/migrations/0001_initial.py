# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habilidades', '0010_auto_20150616_1300'),
        ('usuarios', '0012_auto_20150609_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='teNecesitoModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mensaje', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('habilidadSolicitada', models.ForeignKey(to='habilidades.habilidadesModel')),
                ('usuarioRequerido', models.ForeignKey(related_name=b'requerido', to='usuarios.perfilUsuarioModel')),
                ('usuarioSolicitante', models.ForeignKey(related_name=b'solicitante', to='usuarios.perfilUsuarioModel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
