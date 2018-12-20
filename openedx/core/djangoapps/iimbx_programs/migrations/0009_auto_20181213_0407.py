# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iimbx_programs', '0008_auto_20181213_0225'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='max_hours_effort_per_week',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='program',
            name='min_hours_effort_per_week',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='program',
            name='weeks_to_complete',
            field=models.PositiveSmallIntegerField(help_text='Estimated number of weeks needed to complete a course run belonging to this program.', null=True, blank=True),
        ),
    ]
