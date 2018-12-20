# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slidder', '0004_auto_20181219_0052'),
    ]

    operations = [
      
        migrations.RemoveField(
            model_name='indexslidder',
            name='course',
        ),
        migrations.AddField(
            model_name='indexslidder',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True,serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexslidder',
            name='link',
            field=models.CharField(max_length=800, null=True, blank=True),
        ),
    ]
