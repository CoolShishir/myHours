# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0012_user_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='UserPic',
            field=models.ImageField(default='/home/shishir/Pictures/', upload_to='/home/shishir/Documents/shishir/project/static/images'),
        ),
    ]
