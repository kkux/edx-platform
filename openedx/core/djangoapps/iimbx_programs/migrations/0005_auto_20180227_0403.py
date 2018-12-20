# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iimbx_programs', '0004_auto_20180207_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='active',
            field=models.BooleanField(default=1),
        ),
        migrations.AddField(
            model_name='program',
            name='brochure',
            field=models.FileField(null=True, upload_to=b'media', blank=True),
        ),
    ]
