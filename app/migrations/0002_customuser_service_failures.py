# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-06 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='service_failures',
            field=models.TextField(null=True),
        ),
    ]
