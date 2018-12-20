# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import openedx.core.djangoapps.micro_masters.models
import django.db.models.deletion
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('micro_masters', '0004_auto_20170712_0307'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramCertificateHtmlViewConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('change_date', models.DateTimeField(auto_now_add=True, verbose_name='Change date')),
                ('enabled', models.BooleanField(default=False, verbose_name='Enabled')),
                ('configuration', models.TextField(default=b'{"accomplishment_class_append": "accomplishment-certificate",        "company_about_url": "http://www.example.com/about-us",        "company_privacy_url": "http://www.example.com/privacy-policy",        "company_tos_url": "http://www.example.com/terms-service",        "company_verified_certificate_url": "http://www.example.com/verified-certificate",        "logo_src": "/static/certificates/images/logo.png",        "logo_url": "http://www.example.com",        "platform_name": "Your Platform Name Here",        "certificate_title": "Certificate of Achievement"}', help_text=b'Program Certificate HTML View Parameters (JSON)')),
                ('changed_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='Changed by')),
            ],
            options={
                'ordering': ('-change_date',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProgramCertificateSignatories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(help_text=b'The name of this signatory as it should appear on certificates.', max_length=150)),
                ('title', models.CharField(help_text=b'Titles more than 100 characters may prevent students from printing their certificate on a single page.', max_length=100)),
                ('signature_image', models.ImageField(max_length=200, upload_to=openedx.core.djangoapps.micro_masters.models.content_file_name)),
                ('institution', models.ForeignKey(help_text=b'The organization that this signatory belongs to, as it should appear on certificates.', to='micro_masters.Institution')),
                ('program', models.ForeignKey(to='micro_masters.Program')),
            ],
            options={
                'verbose_name': 'Program Certificate Signatories',
                'verbose_name_plural': 'Program Certificate Signatories',
            },
        ),
        migrations.CreateModel(
            name='ProgramGeneratedCertificate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('issued', models.BooleanField(default=False)),
                ('program', models.ForeignKey(to='micro_masters.Program')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Program Generated Certificate',
                'verbose_name_plural': 'Program Generated Certificate',
            },
        ),
    ]
