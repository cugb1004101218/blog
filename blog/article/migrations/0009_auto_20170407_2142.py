# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 13:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20170406_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('literal', models.CharField(blank=True, max_length=200)),
                ('summary', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_article', to='article.Category'),
        ),
    ]
