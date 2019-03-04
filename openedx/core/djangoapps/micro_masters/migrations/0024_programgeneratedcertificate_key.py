# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_masters', '0023_programgeneratedcertificate_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='programgeneratedcertificate',
            name='key',
            field=models.CharField(default=b'', max_length=32, blank=True),
        ),
    ]
