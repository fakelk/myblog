# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 04:38
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]