# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='dev_type',
            field=models.CharField(max_length=200, choices=[(b'NPI', b'New Product Introdcution'), (b'PI', b'Product Improvement'), (b'SUPPORT', b'Support'), (b'SPL', b'SPL'), (b'OTHER', b'Other')]),
        ),
        migrations.AlterField(
            model_name='project',
            name='market',
            field=models.CharField(max_length=200, choices=[(b'OUTDOOR', b'Outdoor'), (b'INDOOR', b'Indoor'), (b'CONTROLS', b'Controls'), (b'LUMENAREA', b'Lumenarea'), (b'LUMENALPHA', b'Lumenalpha')]),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(max_length=200, choices=[(b'PREGATE', b'Pre-Gate'), (b'GATE1', b'Gate 1'), (b'GATE2', b'Gate 2'), (b'GATE3', b'Gate 3'), (b'GATE4', b'Gate 4'), (b'CLOSED', b'Launched')]),
        ),
    ]
