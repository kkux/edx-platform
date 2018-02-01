# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_auto_20180125_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name_in_arabic',
            field=models.CharField(db_index=True, max_length=255, blank=True),
        ),
    ]
