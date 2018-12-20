# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import openedx.core.djangoapps.micro_masters.models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_masters', '0018_auto_20170911_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='banner_image',
            field=models.ImageField(max_length=200, null=True, upload_to=openedx.core.djangoapps.micro_masters.models.content_file_name, blank=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='sample_certificate_pdf',
            field=models.FileField(null=True, upload_to=openedx.core.djangoapps.micro_masters.models.content_file_name, blank=True),
        ),
    ]
