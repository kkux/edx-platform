# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_overviews', '0015_courseoverview_short_description_in_arabic'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseoverview',
            name='display_name_in_arabic',
            field=models.TextField(null=True),
        ),
    ]
