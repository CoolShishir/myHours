# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 07:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0007_auto_20170418_0659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='id',
            new_name='Id',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='id',
            new_name='Id',
        ),
    ]
