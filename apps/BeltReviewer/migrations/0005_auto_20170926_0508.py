# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-26 05:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BeltReviewer', '0004_auto_20170926_0458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='users',
        ),
        migrations.AddField(
            model_name='review',
            name='users',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='book_reviews', to='BeltReviewer.Book'),
            preserve_default=False,
        ),
    ]
