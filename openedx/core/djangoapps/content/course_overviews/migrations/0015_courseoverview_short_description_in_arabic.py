# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_overviews', '0014_courseoverview_course_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseoverview',
            name='short_description_in_arabic',
            field=models.TextField(null=True),
        ),
    ]
