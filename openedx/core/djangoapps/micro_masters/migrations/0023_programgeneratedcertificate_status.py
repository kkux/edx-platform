# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_masters', '0022_auto_20190131_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='programgeneratedcertificate',
            name='status',
            field=models.CharField(default=b'unavailable', max_length=32),
        ),
    ]
