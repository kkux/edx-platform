# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('iimbx_programs', '0005_auto_20180227_0403'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramApplicant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('username', models.CharField(error_messages={b'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator(b'^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', b'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('mobile', models.CharField(max_length=20, verbose_name='mobile number', blank=True)),
                ('year_of_birth', models.IntegerField(db_index=True, null=True, blank=True)),
                ('gender', models.CharField(blank=True, max_length=6, null=True, db_index=True, choices=[(b'm', b'Male'), (b'f', b'Female'), (b'o', b'Other/Prefer Not to Say')])),
                ('postal_address', models.TextField(null=True, blank=True)),
                ('level_of_education', models.CharField(db_index=True, max_length=128, blank=True)),
                ('discipline_or_stream', models.CharField(db_index=True, max_length=128, blank=True)),
                ('degree', models.CharField(db_index=True, max_length=128, blank=True)),
                ('percentage', models.CharField(db_index=True, max_length=12, blank=True)),
                ('educational_institute', models.CharField(db_index=True, max_length=128, blank=True)),
                ('referencer', models.TextField(null=True, blank=True)),
                ('expectation', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='ProgramFeature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('image', models.ImageField(null=True, upload_to=b'media', blank=True)),
                ('title', models.CharField(max_length=150, blank=True)),
                ('description', models.TextField(help_text='Content in program_feature', null=True, blank=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='ProgramReviewer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('image', models.ImageField(null=True, upload_to=b'media', blank=True)),
                ('name', models.CharField(max_length=150, blank=True)),
                ('review', models.TextField(help_text='Content in review_box', null=True, blank=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.AddField(
            model_name='program',
            name='fee',
            field=models.CharField(default='NA', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='program',
            name='infobox_one_content',
            field=models.TextField(help_text='Content in first infobox', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='program',
            name='infobox_one_title',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='program',
            name='infobox_three_content',
            field=models.TextField(help_text='Content in third infobox', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='program',
            name='infobox_three_title',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='program',
            name='infobox_two_content',
            field=models.TextField(help_text='Content in second infobox', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='program',
            name='infobox_two_title',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='program',
            name='start_date',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='programreviewer',
            name='program_page_content',
            field=models.ForeignKey(to='iimbx_programs.Program'),
        ),
        migrations.AddField(
            model_name='programfeature',
            name='program_page_content',
            field=models.ForeignKey(to='iimbx_programs.Program'),
        ),
    ]
