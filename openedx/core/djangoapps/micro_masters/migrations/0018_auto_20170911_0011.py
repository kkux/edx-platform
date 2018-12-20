# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import openedx.core.djangoapps.micro_masters.models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_masters', '0017_auto_20170910_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='instructors',
            field=models.ManyToManyField(to='micro_masters.Instructor', blank=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='introductory_video',
            field=models.FileField(null=True, upload_to=openedx.core.djangoapps.micro_masters.models.content_file_name, blank=True),
        ),
    ]
