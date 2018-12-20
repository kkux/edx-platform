# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_masters', '0002_programcoupon_programcouponredemption'),
    ]

    operations = [
        migrations.AddField(
            model_name='programorder',
            name='discounted_price',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
