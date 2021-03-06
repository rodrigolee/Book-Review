# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 01:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beltreview', '0006_auto_20170301_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='beltreview.Author'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='book',
            name='review',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=45),
        ),
    ]
