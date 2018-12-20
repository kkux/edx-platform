# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slidder', '0003_auto_20181218_0734'),
    ]

    operations = [
        
        migrations.RemoveField(
            model_name='indexslidder',
            name='description',
        ),
        migrations.AddField(
            model_name='indexslidder',
            name='arabic_image',
            field=models.ImageField(upload_to=b'media'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexslidder',
            name='button_text_in_arabic',
            field=models.CharField( max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexslidder',
            name='button_text_in_english',
            field=models.CharField( max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexslidder',
            name='description_in_arabic',
            field=models.CharField( max_length=800),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexslidder',
            name='description_in_english',
            field=models.CharField(max_length=800),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexslidder',
            name='english_image',
            field=models.ImageField(upload_to=b'media'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexslidder',
            name='title_in_arabic',
            field=models.CharField(max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexslidder',
            name='title_in_english',
            field=models.CharField(max_length=300),
            preserve_default=False,
        ),
    ]
