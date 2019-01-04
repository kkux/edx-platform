# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_userprofile_name_in_arabic'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='force_to_update',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, max_length=6, null=True, db_index=True, choices=[(b'm', b'Male'), (b'f', b'Female')]),
        ),
    ]
