# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_masters', '0008_subject_mark_as_popular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='overview',
            field=models.TextField(default=b'<section class="overview">\n        <h3 class="overview-title">\n            Dummay text.\n        </h3>\n        <div class="overview-content">\n            <p>\n                This is paragraph 2 of the long course description. Add more paragraphs as needed. Make sure to enclose them in paragraph tags.\n            </p>\n        </div>\n    </section>\n    <section class="job-outlook">\n        <h3>About This Path</h3>\n        <ul>\n            <li>\n                This is paragraph 2 of the long course description. Add more paragraphs as needed. Make sure to enclose them in li tags.\n            </li>\n            <li>\n                This is paragraph 2 of the long course description. Add more paragraphs as needed. Make sure to enclose them in li tags.\n            </li>\n            <li>\n                This is paragraph 2 of the long course description. Add more paragraphs as needed. Make sure to enclose them in li tags.\n            </li>\n        </ul>\n    </section>\n    <section class="expected-learning">\n        <h3>Overview:</h3>\n        <ul>\n            <li>This is paragraph 2 of the long course description. Add more paragraphs as needed. Make sure to enclose them in li tags.</li>\n            <li>This is paragraph 2 of the long course description. Add more paragraphs as needed. Make sure to enclose them in li tags.</li>\n            <li>This is paragraph 2 of the long course description. Add more paragraphs as needed. Make sure to enclose them in li tags.</li>\n            <li>How to do full-stack software development using an agile approach in a pair or team</li>\n            <li>This is paragraph 2 of the long course description. Add more paragraphs as needed. Make sure to enclose them in li tags.</li>\n        </ul>\n    </section>\n    ', null=True, blank=True),
        ),
    ]
