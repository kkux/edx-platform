# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_masters', '0005_programcertificatehtmlviewconfiguration_programcertificatesignatories_programgeneratedcertificate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programcertificatehtmlviewconfiguration',
            name='changed_by',
        ),
        migrations.DeleteModel(
            name='ProgramCertificateHtmlViewConfiguration',
        ),
    ]
