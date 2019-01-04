# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slidder', '0005_auto_20181219_0436'),
    ]

    operations = [
        migrations.DeleteModel(
            name='slidderdata',
        ),
    ]
