# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_corso_richieste_particolari'),
    ]

    operations = [
        migrations.AddField(
            model_name='corso',
            name='convalida',
            field=models.BooleanField(default=False),
        ),
    ]
