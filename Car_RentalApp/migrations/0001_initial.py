# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Car_RentalApp.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(db_column='name', max_length=255)),
                ('rent', models.FloatField(db_column='rent')),
                ('model', models.CharField(db_column='model', max_length=255)),
                ('doors', models.IntegerField(db_column='doors')),
                ('seats', models.IntegerField(db_column='seats')),
                ('luggage', models.CharField(db_column='luggage', max_length=255)),
                ('air_condition', models.BooleanField(db_column='air_condition')),
                ('minimum_age', models.IntegerField(db_column='minimum_age')),
                ('image', models.ImageField(upload_to=Car_RentalApp.models.upload_to, db_column='image')),
            ],
            options={
                'db_table': 'Car',
            },
        ),
        migrations.CreateModel(
            name='Car_Reservation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('source', models.CharField(db_column='source', max_length=255)),
                ('destination', models.CharField(db_column='destination', max_length=255)),
                ('pick_up_time', models.DateTimeField(db_column='pick_up_time')),
                ('dropping_time', models.DateTimeField(db_column='dropping_time')),
                ('created', models.DateTimeField(db_column='created_at', auto_now_add=True)),
                ('car', models.ForeignKey(to='Car_RentalApp.Car', related_name='cars')),
            ],
            options={
                'db_table': 'Car_Reservation',
            },
        ),
        migrations.CreateModel(
            name='Customer_Care_Representative',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(db_column='name', max_length=255)),
                ('phone', models.CharField(db_column='phone', max_length=13)),
                ('email', models.EmailField(db_column='email', max_length=254)),
                ('image', models.ImageField(upload_to=Car_RentalApp.models.upload_to, db_column='image')),
                ('staff_type', models.CharField(choices=[('VOICE SUPPORT', 'VOICE SUPPORT'), ('TECHNICAL SUPPORT', 'TECHNICAL SUPPORT')], default='VOICE SUPPORT', db_column='type', max_length=25)),
            ],
            options={
                'db_table': 'Customer_Care',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('first_name', models.CharField(db_column='first_name', max_length=255)),
                ('last_name', models.CharField(db_column='last_name', max_length=255)),
                ('phone', models.CharField(db_column='phone', max_length=13)),
                ('email', models.EmailField(db_column='email', max_length=254)),
                ('message', models.TextField(db_column='message')),
            ],
            options={
                'db_table': 'Feedback',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('first_name', models.CharField(db_column='first_name', max_length=255)),
                ('last_name', models.CharField(db_column='last_name', max_length=255)),
                ('phone', models.CharField(db_column='phone', max_length=13)),
                ('age', models.IntegerField(db_column='age')),
                ('email', models.EmailField(db_column='email', max_length=254)),
                ('address', models.CharField(db_column='address', max_length=512)),
                ('city', models.CharField(db_column='city', max_length=128)),
                ('zip_code', models.CharField(db_column='zip_code', max_length=15)),
            ],
            options={
                'db_table': 'Person',
            },
        ),
        migrations.AddField(
            model_name='car_reservation',
            name='person',
            field=models.ForeignKey(to='Car_RentalApp.Person', related_name='persons'),
        ),
    ]
