# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iimbx_programs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programcategory',
            name='position',
            field=models.IntegerField(help_text=b'Higher priority a smaller number'),
        ),
    ]
