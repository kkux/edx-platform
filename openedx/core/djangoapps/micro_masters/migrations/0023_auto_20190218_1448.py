# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_masters', '0022_auto_20190131_0027'),
    ]

    operations = [
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
            model_name='programcertificatesignatories',
            name='signature_image',
            field=models.ImageField(max_length=200, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='programorder',
            name='currency',
            field=models.CharField(default=['sar', '&#65020;'], max_length=30, blank=True),
        ),
    ]
