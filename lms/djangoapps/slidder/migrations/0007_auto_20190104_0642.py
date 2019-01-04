# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slidder', '0006_delete_slidderdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indexslidder',
            old_name='link',
            new_name='link_arabic',
        ),
        migrations.AddField(
            model_name='indexslidder',
            name='link_english',
            field=models.CharField(max_length=800, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='indexslidder',
            name='arabic_image',
            field=models.ImageField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='indexslidder',
            name='english_image',
            field=models.ImageField(upload_to=b''),
        ),
    ]
