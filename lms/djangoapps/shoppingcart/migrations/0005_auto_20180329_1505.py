# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0004_auto_20180125_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceitem',
            name='currency',
            field=models.CharField(default=b'sar', help_text='Lower-case ISO currency codes', max_length=8),
        ),
        migrations.AlterField(
            model_name='invoicetransaction',
            name='currency',
            field=models.CharField(default=b'sar', help_text='Lower-case ISO currency codes', max_length=8),
        ),
        migrations.AlterField(
            model_name='order',
            name='currency',
            field=models.CharField(default=b'sar', max_length=8),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='currency',
            field=models.CharField(default=b'sar', max_length=8),
        ),
    ]
