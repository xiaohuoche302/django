# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-16 14:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study05', '0008_auto_20180716_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contents',
            name='content_num',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='study05.Movies', verbose_name='集数'),
        ),
    ]
