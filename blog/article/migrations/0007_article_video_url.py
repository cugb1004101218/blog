# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 00:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_article_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='video_url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]