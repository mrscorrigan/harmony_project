# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Styleme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('description', models.TextField()),
                ('image', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
