# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0003_auto_20151217_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='bill_to_country_code',
            field=models.CharField(max_length=8, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='bill_to_phone_number',
            field=models.CharField(max_length=16, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='ip_customer',
            field=models.CharField(max_length=240, blank=True),
        ),
    ]
