# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kkux', '0002_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribers',
            name='activated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='subscribers',
            name='activation_code',
            field=models.CharField(default=1, max_length=512),
            preserve_default=False,
        ),
    ]
