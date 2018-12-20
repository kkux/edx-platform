# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_masters', '0006_auto_20170712_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='programgeneratedcertificate',
            name='verify_uuid',
            field=models.CharField(default=b'', max_length=32, db_index=True, blank=True),
        ),
    ]
