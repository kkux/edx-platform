# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iimbx_programs', '0006_auto_20180419_2311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='infobox_one_content',
        ),
        migrations.RemoveField(
            model_name='program',
            name='infobox_one_title',
        ),
        migrations.RemoveField(
            model_name='program',
            name='infobox_three_content',
        ),
        migrations.RemoveField(
            model_name='program',
            name='infobox_three_title',
        ),
        migrations.RemoveField(
            model_name='program',
            name='infobox_two_content',
        ),
        migrations.RemoveField(
            model_name='program',
            name='infobox_two_title',
        ),
        migrations.AddField(
            model_name='program',
            name='expected_learning',
            field=models.TextField(help_text='expected Learning', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='program',
            name='job_Outlook',
            field=models.TextField(help_text='Job Outlook', null=True, blank=True),
        ),
    ]
