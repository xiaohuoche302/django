# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-20 06:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study05', '0012_auto_20180719_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contents',
            name='content_num',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='study05.Movies', verbose_name='集数'),
        ),
    ]
