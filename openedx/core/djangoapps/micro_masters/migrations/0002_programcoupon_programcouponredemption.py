# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('micro_masters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramCoupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('code', models.CharField(max_length=32, db_index=True)),
                ('description', models.CharField(max_length=255, null=True, blank=True)),
                ('percentage_discount', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('expiration_date', models.DateTimeField(null=True, blank=True)),
                ('program', models.ForeignKey(to='micro_masters.Program')),
            ],
            options={
                'verbose_name': 'Program Coupon',
                'verbose_name_plural': 'Program Coupons',
            },
        ),
        migrations.CreateModel(
            name='ProgramCouponRedemption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('coupon', models.ForeignKey(to='micro_masters.ProgramCoupon')),
                ('order', models.ForeignKey(to='micro_masters.ProgramOrder')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Program Coupon Redemption',
                'verbose_name_plural': 'Program Coupon Redemptions',
            },
        ),
    ]
