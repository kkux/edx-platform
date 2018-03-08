# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0010_auto_20180130_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='generatedcertificate',
            name='name_in_arabic',
            field=models.CharField(max_length=512, blank=True),
        ),
    ]
