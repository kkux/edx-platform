# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_masters', '0024_programgeneratedcertificate_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='programgeneratedcertificate',
            name='candidate_serialno',
            field=models.CharField(default=0, max_length=8, db_index=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='logo',
            field=models.ImageField(max_length=200, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='profile_image',
            field=models.ImageField(max_length=200, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='program',
            name='introductory_video',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='sample_certificate_pdf',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='programcertificatesignatories',
            name='signature_image',
            field=models.ImageField(max_length=200, upload_to=b''),
        ),
    ]
