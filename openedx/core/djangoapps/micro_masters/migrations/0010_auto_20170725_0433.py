# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_masters', '0009_auto_20170725_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='programorder',
            name='item_name',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='programorder',
            name='item_price',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
