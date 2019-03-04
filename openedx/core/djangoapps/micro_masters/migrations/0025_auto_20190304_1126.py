# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_masters', '0024_auto_20190304_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='name_arabic',
            field=models.CharField( unique=True, max_length=200,verbose_name="name in arabic"),
            preserve_default=False,
        ),
    ]
