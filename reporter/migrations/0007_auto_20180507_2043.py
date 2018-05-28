# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-07 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0006_auto_20180507_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fiberboxes',
            name='towns',
        ),
        migrations.AddField(
            model_name='fiberboxes',
            name='town',
            field=models.CharField(blank=True, max_length=50, verbose_name='\u4e61\u9547\uff08\u533a\uff09'),
        ),
        migrations.AlterField(
            model_name='fiberboxes',
            name='village',
            field=models.CharField(blank=True, max_length=50, verbose_name='\u6751\uff08\u8857\uff09'),
        ),
    ]