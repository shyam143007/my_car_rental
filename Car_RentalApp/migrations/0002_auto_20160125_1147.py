# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Car_RentalApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 25, 6, 16, 18, 310501, tzinfo=utc), db_column='created', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='is_active',
            field=models.BooleanField(default=1, db_column='is_active'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer_care_representative',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 25, 6, 16, 54, 130393, tzinfo=utc), db_column='created', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer_care_representative',
            name='is_active',
            field=models.BooleanField(default=1, db_column='is_active'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 25, 6, 17, 10, 426338, tzinfo=utc), db_column='created', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 25, 6, 17, 25, 759040, tzinfo=utc), db_column='created', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='is_active',
            field=models.BooleanField(default=1, db_column='is_active'),
            preserve_default=False,
        ),
    ]
