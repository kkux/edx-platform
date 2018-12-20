# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_masters', '0010_auto_20170725_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='institution',
            field=models.ForeignKey(default=1, to='micro_masters.Institution'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='language',
            name='code',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='program',
            name='short_description',
            field=models.TextField(help_text=b'Appears on the program about page. Limit to ~150 characters', max_length=150, null=True, blank=True),
        ),
    ]
