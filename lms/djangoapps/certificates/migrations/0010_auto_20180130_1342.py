# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import certificates.models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0009_generatedcertificate_candidate_serial_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generatedcertificate',
            name='candidate_serial_no',
            field=models.CharField(default=certificates.models.increment_serial_number, max_length=8, db_index=True),
        ),
    ]
