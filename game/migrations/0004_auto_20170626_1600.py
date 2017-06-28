# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-26 16:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_hint'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('detail', models.TextField(max_length=1000)),
                ('answer', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='round',
            old_name='question',
            new_name='detail',
        ),
        migrations.RenameField(
            model_name='round',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='question',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Round'),
        ),
    ]
