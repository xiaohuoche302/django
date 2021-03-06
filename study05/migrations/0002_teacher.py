# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-13 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study05', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='人名')),
                ('age', models.IntegerField(default=1, verbose_name='年纪')),
                ('sex', models.CharField(max_length=6, verbose_name='性别')),
                ('salary', models.IntegerField(verbose_name='工资S')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
