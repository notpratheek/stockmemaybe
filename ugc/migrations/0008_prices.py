# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0007_auto_20150329_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('price', models.FloatField()),
                ('time', models.DateTimeField()),
                ('company', models.ForeignKey(to='ugc.Company')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
