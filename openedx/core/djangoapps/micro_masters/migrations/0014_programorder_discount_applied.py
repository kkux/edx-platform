# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_masters', '0013_auto_20170808_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='programorder',
            name='discount_applied',
            field=models.BooleanField(default=0),
        ),
    ]
