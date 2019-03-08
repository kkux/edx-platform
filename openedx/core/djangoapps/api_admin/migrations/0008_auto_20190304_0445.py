# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_admin', '0007_auto_20181214_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiaccessrequest',
            name='reason',
            field=models.TextField(help_text='The reason this user wants to access the API.'),
        ),
        migrations.AlterField(
            model_name='apiaccessrequest',
            name='status',
            field=models.CharField(default=b'pending', help_text='Status of this API access request', max_length=255, db_index=True, choices=[(b'pending', 'Pending'), (b'denied', 'Denied'), (b'approved', 'Approved')]),
        ),
        migrations.AlterField(
            model_name='apiaccessrequest',
            name='website',
            field=models.URLField(help_text='The URL of the website associated with this API user.'),
        ),
        migrations.AlterField(
            model_name='historicalapiaccessrequest',
            name='reason',
            field=models.TextField(help_text='The reason this user wants to access the API.'),
        ),
        migrations.AlterField(
            model_name='historicalapiaccessrequest',
            name='status',
            field=models.CharField(default=b'pending', help_text='Status of this API access request', max_length=255, db_index=True, choices=[(b'pending', 'Pending'), (b'denied', 'Denied'), (b'approved', 'Approved')]),
        ),
        migrations.AlterField(
            model_name='historicalapiaccessrequest',
            name='website',
            field=models.URLField(help_text='The URL of the website associated with this API user.'),
        ),
    ]
