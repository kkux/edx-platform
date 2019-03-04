# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_masters', '0026_auto_20190225_0337'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='name_in_arabic',
            field=models.CharField( unique=True, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='program',
            name='name',
            field=models.CharField(unique=True, max_length=200, verbose_name=b'name in english'),
        ),
    ]
