# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import openedx.core.djangoapps.micro_masters.models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_masters', '0023_auto_20190218_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='name_arabic',
            field=models.CharField( unique=True, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programgeneratedcertificate',
            name='candidate_serialno',
            field=models.CharField(default=openedx.core.djangoapps.micro_masters.models.increment_serial_number, max_length=8, db_index=True),
        ),
        migrations.AddField(
            model_name='programgeneratedcertificate',
            name='key',
            field=models.CharField(default=b'', max_length=32, blank=True),
        ),
        migrations.AddField(
            model_name='programgeneratedcertificate',
            name='status',
            field=models.CharField(default=b'unavailable', max_length=32),
        ),
        migrations.AlterField(
            model_name='program',
            name='introductory_video',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='name',
            field=models.CharField(unique=True, max_length=200, verbose_name=b'name in english'),
        ),
        migrations.AlterField(
            model_name='program',
            name='sample_certificate_pdf',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
