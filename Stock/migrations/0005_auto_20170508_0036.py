# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 22:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0004_auto_20170508_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinestock',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.Branches'),
        ),
    ]