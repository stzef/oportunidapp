# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habilidades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='teNecesitoModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mensaje', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('habilidadSolicitada', models.ForeignKey(to='habilidades.habilidadesModel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
