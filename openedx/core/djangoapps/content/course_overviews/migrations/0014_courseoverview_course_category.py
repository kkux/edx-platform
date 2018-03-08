# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_overviews', '0013_courseoverview_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseoverview',
            name='course_category',
            field=models.TextField(null=True),
        ),
    ]
