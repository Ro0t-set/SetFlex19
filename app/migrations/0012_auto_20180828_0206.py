# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-28 00:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20180828_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corso',
            name='convalida1',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='corso',
            name='convalida2',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='corso',
            name='convalida3',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='corso',
            name='convalida4',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='corso',
            name='convalida5',
            field=models.BooleanField(default=False),
        ),
    ]
