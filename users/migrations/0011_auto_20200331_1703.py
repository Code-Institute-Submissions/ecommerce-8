# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-31 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200331_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]