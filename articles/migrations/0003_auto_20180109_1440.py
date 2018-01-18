# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-09 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20180109_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_photosrc',
            field=models.URLField(max_length=300),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_site',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_url',
            field=models.URLField(max_length=300),
        ),
    ]