# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-12 01:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='名字')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('count', models.IntegerField(verbose_name='火力输出')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=30, verbose_name='球队名')),
                ('contry', models.CharField(max_length=30, verbose_name='所属国家')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='study03.Team', verbose_name='所属球队'),
        ),
    ]
