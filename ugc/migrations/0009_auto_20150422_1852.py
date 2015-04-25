# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0008_prices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prices',
            name='company',
        ),
        migrations.DeleteModel(
            name='Prices',
        ),
    ]
