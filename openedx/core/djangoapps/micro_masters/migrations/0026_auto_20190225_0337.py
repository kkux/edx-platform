# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import openedx.core.djangoapps.micro_masters.models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_masters', '0025_auto_20190225_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programgeneratedcertificate',
            name='candidate_serialno',
            field=models.CharField(default=openedx.core.djangoapps.micro_masters.models.increment_serial_number, max_length=8, db_index=True),
        ),
    ]
