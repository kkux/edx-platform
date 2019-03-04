# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_admin', '0006_catalog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiaccessrequest',
            name='reason',
            field=models.TextField(help_text='\u0627\u0644\u0633\u0628\u0628 \u0648\u0631\u0627\u0621 \u0631\u063a\u0628\u0629 \u0647\u0630\u0627 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645 \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 \u0648\u0627\u062c\u0647\u0629 \u0627\u0644\u062a\u0637\u0628\u064a\u0642 \u0627\u0644\u0628\u0631\u0645\u062c\u064a\u0629.'),
        ),
        migrations.AlterField(
            model_name='apiaccessrequest',
            name='status',
            field=models.CharField(default=b'pending', help_text='\u062d\u0627\u0644\u0629 \u0637\u0644\u0628 \u0627\u0644\u0648\u0635\u0648\u0644 \u0627\u0644\u062e\u0627\u0635 \u0628\u0648\u0627\u062c\u0647\u0629 \u0627\u0644\u062a\u0637\u0628\u064a\u0642 \u0627\u0644\u0628\u0631\u0645\u062c\u064a\u0629.', max_length=255, db_index=True, choices=[(b'pending', '\u0642\u064a\u062f \u0627\u0644\u0627\u0646\u062a\u0638\u0627\u0631'), (b'denied', '\u0645\u0631\u0641\u0648\u0636'), (b'approved', '\u0645\u0648\u0627\u0641\u0642 \u0639\u0644\u064a\u0647')]),
        ),
        migrations.AlterField(
            model_name='apiaccessrequest',
            name='website',
            field=models.URLField(help_text='\u0631\u0627\u0628\u0637 \u0627\u0644\u0645\u0648\u0642\u0639 \u0627\u0644\u0625\u0644\u0643\u062a\u0631\u0648\u0646\u064a \u0627\u0644\u0645\u0631\u062a\u0628\u0637 \u0628\u0645\u0633\u062a\u062e\u062f\u0645 \u0648\u0627\u062c\u0647\u0629 \u0627\u0644\u062a\u0637\u0628\u064a\u0642 \u0627\u0644\u0628\u0631\u0645\u062c\u064a\u0629 \u0647\u0630\u0647.'),
        ),
        migrations.AlterField(
            model_name='historicalapiaccessrequest',
            name='reason',
            field=models.TextField(help_text='\u0627\u0644\u0633\u0628\u0628 \u0648\u0631\u0627\u0621 \u0631\u063a\u0628\u0629 \u0647\u0630\u0627 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645 \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 \u0648\u0627\u062c\u0647\u0629 \u0627\u0644\u062a\u0637\u0628\u064a\u0642 \u0627\u0644\u0628\u0631\u0645\u062c\u064a\u0629.'),
        ),
        migrations.AlterField(
            model_name='historicalapiaccessrequest',
            name='status',
            field=models.CharField(default=b'pending', help_text='\u062d\u0627\u0644\u0629 \u0637\u0644\u0628 \u0627\u0644\u0648\u0635\u0648\u0644 \u0627\u0644\u062e\u0627\u0635 \u0628\u0648\u0627\u062c\u0647\u0629 \u0627\u0644\u062a\u0637\u0628\u064a\u0642 \u0627\u0644\u0628\u0631\u0645\u062c\u064a\u0629.', max_length=255, db_index=True, choices=[(b'pending', '\u0642\u064a\u062f \u0627\u0644\u0627\u0646\u062a\u0638\u0627\u0631'), (b'denied', '\u0645\u0631\u0641\u0648\u0636'), (b'approved', '\u0645\u0648\u0627\u0641\u0642 \u0639\u0644\u064a\u0647')]),
        ),
        migrations.AlterField(
            model_name='historicalapiaccessrequest',
            name='website',
            field=models.URLField(help_text='\u0631\u0627\u0628\u0637 \u0627\u0644\u0645\u0648\u0642\u0639 \u0627\u0644\u0625\u0644\u0643\u062a\u0631\u0648\u0646\u064a \u0627\u0644\u0645\u0631\u062a\u0628\u0637 \u0628\u0645\u0633\u062a\u062e\u062f\u0645 \u0648\u0627\u062c\u0647\u0629 \u0627\u0644\u062a\u0637\u0628\u064a\u0642 \u0627\u0644\u0628\u0631\u0645\u062c\u064a\u0629 \u0647\u0630\u0647.'),
        ),
    ]
