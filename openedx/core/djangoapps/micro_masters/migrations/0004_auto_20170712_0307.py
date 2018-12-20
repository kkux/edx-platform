# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_masters', '0003_programorder_discounted_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programorder',
            name='discounted_price',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
