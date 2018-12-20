# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_masters', '0014_programorder_discount_applied'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='courses',
            unique_together=set([('course_key', 'name')]),
        ),
    ]
