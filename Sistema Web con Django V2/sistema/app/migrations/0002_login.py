# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=150)),
                ('clave', models.CharField(max_length=150)),
            ],
            options={
                'managed': False,
            },
        ),
    ]
