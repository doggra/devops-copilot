# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 01:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_auto_20171021_2223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='stats',
        ),
        migrations.AddField(
            model_name='serverstats',
            name='server',
            field=models.ForeignKey(default='6470bbcf-4b7f-4928-818d-32b7d91b94b7', on_delete=django.db.models.deletion.CASCADE, to='server.Server'),
            preserve_default=False,
        ),
    ]