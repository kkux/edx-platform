# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0003_auto_20160511_2227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creditrequirementstatus',
            options={'verbose_name_plural': '\u062d\u0627\u0644\u0627\u062a \u0645\u062a\u0637\u0644\u0628\u0627\u062a \u0627\u0644\u0627\u0639\u062a\u0645\u0627\u062f'},
        ),
        migrations.AlterField(
            model_name='creditconfig',
            name='cache_ttl',
            field=models.PositiveIntegerField(default=0, help_text='\u0645\u062d\u062f\u0651\u062f \u0628\u0627\u0644\u062b\u0648\u0627\u0646\u064a. \u0641\u0639\u0651\u0644 \u0645\u064a\u0632\u0629 \u0627\u0644\u0627\u062d\u062a\u0641\u0627\u0638 \u0628\u0627\u0644\u0628\u064a\u0627\u0646\u0627\u062a \u0641\u064a \u0627\u0644\u0630\u0627\u0643\u0631\u0629 \u0627\u0644\u0645\u0624\u0642\u062a\u0629 Cache \u0628\u062a\u0639\u064a\u064a\u0646 \u0647\u0630\u0647 \u0627\u0644\u0642\u064a\u0645\u0629 \u0644\u062a\u0635\u0628\u062d \u0623\u0643\u0628\u0631 \u0645\u0646 0.', verbose_name='\u0645\u062f\u0651\u0629 \u0628\u0642\u0627\u0621 \u0627\u0644\u0628\u064a\u0627\u0646\u0627\u062a \u0641\u064a \u0627\u0644\u0630\u0627\u0643\u0631\u0629 \u0627\u0644\u0645\u0624\u0642\u0651\u062a\u0629 "Cache"'),
        ),
    ]
