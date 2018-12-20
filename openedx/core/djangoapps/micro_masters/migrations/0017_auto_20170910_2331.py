# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_masters', '0016_auto_20170907_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='instructors',
            field=models.ManyToManyField(to='micro_masters.Instructor'),
        ),
    ]
