# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(default=b'English', max_length=50)),
                ('code', models.CharField(default=b'en', unique=True, max_length=10)),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(help_text=b'News title upto 30 characters', max_length=255)),
                ('link', models.URLField(help_text=b'Link for the news')),
                ('short_description', models.TextField(help_text=b'Add description upto 100 characters', null=True, blank=True)),
                ('position', models.IntegerField(default=1, help_text=b'Position/order of the news')),
                ('language', models.ForeignKey(to='kkux.Language')),
            ],
            options={
                'ordering': ['position'],
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
    ]
