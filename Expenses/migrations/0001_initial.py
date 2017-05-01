# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-26 22:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('notes', models.CharField(max_length=200)),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.Pharmacy')),
            ],
        ),
        migrations.AddField(
            model_name='destination',
            name='expenses_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Expenses.Expenses'),
        ),
    ]