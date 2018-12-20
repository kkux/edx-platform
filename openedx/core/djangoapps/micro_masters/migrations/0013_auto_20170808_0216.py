# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_masters', '0012_auto_20170808_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='institution',
            field=models.ForeignKey(default=1, to='micro_masters.Institution'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='program',
            name='language',
            field=models.ForeignKey(related_name='program_language', default=1, to='micro_masters.Language'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='program',
            name='short_description',
            field=models.TextField(default=1, help_text=b'Appears on the program about page. Limit to ~150 characters', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='program',
            name='subject',
            field=models.ForeignKey(default=1, to='micro_masters.Subject'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='program',
            name='video_transcripts',
            field=models.ForeignKey(related_name='transcript_language', default=1, to='micro_masters.Language'),
            preserve_default=False,
        ),
    ]
