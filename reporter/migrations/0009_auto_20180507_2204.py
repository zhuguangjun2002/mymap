# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-07 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0008_auto_20180507_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiberboxes',
            name='village',
            field=models.CharField(blank=True, max_length=50, verbose_name='\u6751\uff08\u793e\u533a\u5c45\u59d4\u4f1a\uff09'),
        ),
    ]
