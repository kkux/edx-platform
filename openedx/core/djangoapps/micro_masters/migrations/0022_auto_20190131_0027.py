# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_masters', '0021_auto_20190123_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programorder',
            name='currency',
            field=models.CharField(default=['sar', 'sar'], max_length=30, blank=True),
        ),
    ]
