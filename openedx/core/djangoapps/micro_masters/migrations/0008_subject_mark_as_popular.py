# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_masters', '0007_programgeneratedcertificate_verify_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='mark_as_popular',
            field=models.BooleanField(default=0),
        ),
    ]
