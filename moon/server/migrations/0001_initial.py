# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 21:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('os', models.IntegerField(choices=[(0, 'Debian'), (1, 'CentOS')], null=True)),
                ('hostname', models.CharField(max_length=255)),
                ('status', models.IntegerField(choices=[(0, 'Install'), (1, 'Ready'), (2, 'Updating'), (3, 'Alert')], default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]