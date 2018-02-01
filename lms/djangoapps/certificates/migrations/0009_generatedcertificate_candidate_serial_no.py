# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0008_schema__remove_badges'),
    ]

    operations = [
        migrations.AddField(
            model_name='generatedcertificate',
            name='candidate_serial_no',
            field=models.CharField(default='AA0001', max_length=8, db_index=True),
            preserve_default=False,
        ),
    ]
