# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20150330_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='habCategoriasModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoria', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='habilidadesModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nhabilidad', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=250)),
                ('val_promedio', models.IntegerField(null=True, blank=True)),
                ('num_solicitudes', models.IntegerField(null=True, blank=True)),
                ('estado', models.CharField(default=1, max_length=1, choices=[(1, b'Activo'), (2, b'Inactivo'), (3, b'Eliminado')])),
                ('precio', models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)),
                ('id_categoria', models.ForeignKey(to='habilidades.habCategoriasModel')),
                ('id_usuario', models.ForeignKey(to='usuarios.perfilUsuarioModel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
