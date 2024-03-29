# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-27 20:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20170626_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaderboard',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='round',
            name='number',
            field=models.IntegerField(unique=True),
        ),
    ]
