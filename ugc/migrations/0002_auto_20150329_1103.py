# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='company',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='source',
        ),
        migrations.DeleteModel(
            name='Messages',
        ),
        migrations.DeleteModel(
            name='Source',
        ),
    ]
