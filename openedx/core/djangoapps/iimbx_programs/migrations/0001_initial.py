# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import openedx.core.djangoapps.xmodule_django.models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('course_key', openedx.core.djangoapps.xmodule_django.models.CourseKeyField(max_length=255)),
                ('display_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=240)),
                ('slug', models.SlugField(help_text=b'This is part of program URL, so no spaces or special characters are allowed', unique=True, max_length=200)),
                ('short_description', models.TextField(help_text=b'Appears on the program mega menu. Limit to ~150 characters', max_length=150)),
                ('image', models.ImageField(upload_to=b'')),
                ('long_description', models.TextField(help_text=b'Appears on the program about page. Limit to ~500 characters', max_length=500)),
                ('courses', models.ManyToManyField(to='iimbx_programs.Courses')),
            ],
            options={
                'verbose_name': 'Program',
                'verbose_name_plural': 'Programs',
            },
        ),
        migrations.CreateModel(
            name='ProgramCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(unique=True, max_length=240)),
                ('position', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Program Category',
                'verbose_name_plural': 'Program Category',
            },
        ),
        migrations.AddField(
            model_name='program',
            name='program_category',
            field=models.ForeignKey(to='iimbx_programs.ProgramCategory'),
        ),
        migrations.AlterUniqueTogether(
            name='courses',
            unique_together=set([('course_key', 'display_name')]),
        ),
    ]
