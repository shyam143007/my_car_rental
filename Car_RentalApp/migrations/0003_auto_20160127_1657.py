# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Car_RentalApp', '0002_auto_20160125_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='is_active',
            field=models.BooleanField(default=True, db_column='is_active'),
        ),
        migrations.AlterField(
            model_name='customer_care_representative',
            name='is_active',
            field=models.BooleanField(default=True, db_column='is_active'),
        ),
        migrations.AlterField(
            model_name='person',
            name='is_active',
            field=models.BooleanField(default=True, db_column='is_active'),
        ),
    ]
