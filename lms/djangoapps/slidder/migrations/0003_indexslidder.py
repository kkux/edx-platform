# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import openedx.core.djangoapps.xmodule_django.models


class Migration(migrations.Migration):

    dependencies = [
        ('slidder', '0002_delete_indexslidder'),
    ]

    operations = [
        migrations.CreateModel(
            name='indexslidder',
            fields=[
                ('course', openedx.core.djangoapps.xmodule_django.models.CourseKeyField(max_length=255, serialize=False, primary_key=True, db_index=True)),
                ('title_in_english', models.CharField(max_length=300)),
                ('title_in_arabic', models.CharField(max_length=300)),
                ('description_in_english', models.CharField(max_length=800)),
                ('description_in_arabic', models.CharField(max_length=800)),
                ('arabic_image', models.ImageField(upload_to=b'')),
                ('english_image', models.ImageField(upload_to=b'')),
                ('button_text_in_english', models.CharField(max_length=30)),
                ('button_text_in_arabic', models.CharField(max_length=30)),
                ('link_arabic', models.CharField(max_length=800, null=True, blank=True)),
                ('link_english', models.CharField(max_length=800, null=True, blank=True)),
            ],
        ),
    ]
