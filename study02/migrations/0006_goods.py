# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-10 12:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study02', '0005_auto_20180710_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('in_datetime', models.DateTimeField(auto_now_add=True, verbose_name='生产日期')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study02.Hyrz', verbose_name='分类')),
            ],
        ),
    ]
