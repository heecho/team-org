# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('capacity', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dept_Hours',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hours', models.IntegerField()),
                ('department', models.ForeignKey(to='projects.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('dev_type', models.CharField(max_length=200)),
                ('market', models.CharField(max_length=200)),
                ('fiscal_year', models.CharField(max_length=4, blank=True)),
                ('description', models.TextField(blank=True)),
                ('pubdate', models.DateField(auto_now_add=True)),
                ('acquisition', models.BooleanField()),
                ('fast_track', models.BooleanField()),
                ('departments', models.ManyToManyField(to='projects.Department', through='projects.Dept_Hours')),
            ],
        ),
        migrations.AddField(
            model_name='dept_hours',
            name='project',
            field=models.ForeignKey(to='projects.Project'),
        ),
    ]
