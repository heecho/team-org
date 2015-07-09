# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20150622_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dept_hours',
            name='hours',
            field=models.IntegerField(blank=True),
        ),
    ]
