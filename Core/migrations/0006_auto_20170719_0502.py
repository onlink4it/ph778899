# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-19 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0005_auto_20170702_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='joined_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='left_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='discount_percent',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coremedicine',
            name='med_unit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='coremedicine',
            name='small_unit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coremedicine',
            name='storage_temp',
            field=models.IntegerField(),
        ),
    ]