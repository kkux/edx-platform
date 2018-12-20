# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('iimbx_programs', '0002_auto_20171228_0326'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramCertificateSignatories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(help_text=b'The name of this signatory as it should appear on certificates.', max_length=150)),
                ('title', models.CharField(help_text=b'Titles more than 100 characters may prevent students from printing their certificate on a single page.', max_length=100)),
                ('institution', models.TextField(help_text=b'The organization that this signatory belongs to, as it should appear on certificates.', max_length=150)),
                ('signature_image', models.ImageField(upload_to=b'')),
                ('program', models.ForeignKey(to='iimbx_programs.Program')),
            ],
            options={
                'verbose_name': 'Program Certificate Signatories',
                'verbose_name_plural': 'Program Certificate Signatories',
            },
        ),
        migrations.CreateModel(
            name='ProgramEnrollment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('is_active', models.BooleanField(default=0)),
                ('program', models.ForeignKey(to='iimbx_programs.Program')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Program Enrollment',
                'verbose_name_plural': 'Program Enrollment',
            },
        ),
    ]
