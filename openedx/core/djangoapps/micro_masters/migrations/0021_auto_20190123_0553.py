# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_masters', '0020_auto_20190123_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programorder',
            name='currency',
            field=models.CharField(default=['usd', '$'], max_length=30, blank=True),
        ),
    ]
