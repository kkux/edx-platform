# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20170207_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='country_code',
            field=models.CharField(max_length=8, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='postalcode',
            field=models.CharField(max_length=16, blank=True),
        ),
    ]
