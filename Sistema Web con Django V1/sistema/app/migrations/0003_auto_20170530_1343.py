# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_registro',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_registro',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_registro',
            field=models.DateField(auto_now_add=True),
        ),
    ]
