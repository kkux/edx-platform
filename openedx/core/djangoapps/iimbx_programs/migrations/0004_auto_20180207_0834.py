# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iimbx_programs', '0003_programcertificatesignatories_programenrollment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='image',
            field=models.ImageField(upload_to=b'media'),
        ),
    ]
