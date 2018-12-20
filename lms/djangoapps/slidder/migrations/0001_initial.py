# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import openedx.core.djangoapps.xmodule_django.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='slidderdata',
            fields=[
                ('course', openedx.core.djangoapps.xmodule_django.models.CourseKeyField(max_length=255, serialize=False, primary_key=True, db_index=True)),
                ('description', models.CharField(max_length=800)),
            ],
        ),
    ]
