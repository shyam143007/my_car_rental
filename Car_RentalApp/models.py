from django.db import models
from datetime import date

# Create your models here.

VOICE_SUPPORT = 'VOICE SUPPORT'
TECHNICAL_SUPPORT = 'TECHNICAL SUPPORT'

STAFF_CHOICES = (
    (VOICE_SUPPORT, 'VOICE SUPPORT'),
    (TECHNICAL_SUPPORT, 'TECHNICAL SUPPORT'),
)


def upload_to(instance, filename):
    name_of_model = type(instance).__name__
    _date = date.today()
    folder = "{}-{}-{}".format(_date.year, _date.month, _date.day)
    return "static/Car_RentalApp/Images/{}/{}/{}".format(name_of_model, folder, filename)


class Person(models.Model):
    first_name = models.CharField(db_column='first_name', max_length=255)
    last_name = models.CharField(db_column='last_name', max_length=255)
    phone = models.CharField(db_column='phone', max_length=13)
    age = models.IntegerField(db_column='age')
    email = models.EmailField(db_column='email', unique=True)
    address = models.CharField(db_column='address', max_length=512)
    city = models.CharField(db_column='city', max_length=128)
    zip_code = models.CharField(db_column='zip_code', max_length=15)
    created = models.DateTimeField(db_column='created', auto_now_add=True)
    is_active = models.BooleanField(db_column='is_active', default=True)

    class Meta:
        db_table = 'Person'


class Car(models.Model):
    name = models.CharField(db_column='name', max_length=255)
    rent = models.FloatField(db_column='rent')
    model = models.CharField(db_column='model', max_length=255)
    doors = models.IntegerField(db_column='doors')
    seats = models.IntegerField(db_column='seats')
    luggage = models.CharField(db_column='luggage', max_length=255)
    air_condition = models.BooleanField(db_column='air_condition')
    minimum_age = models.IntegerField(db_column='minimum_age')
    image = models.ImageField(db_column='image', upload_to=upload_to)
    created = models.DateTimeField(db_column='created', auto_now_add=True)
    is_active = models.BooleanField(db_column='is_active', default=True)
    # transmission = models.

    class Meta:
        db_table = 'Car'


class Car_Reservation(models.Model):
    source = models.CharField(max_length=255, db_column='source')
    destination = models.CharField(max_length=255, db_column='destination')
    pick_up_time = models.DateTimeField(db_column='pick_up_time')
    dropping_time = models.DateTimeField(db_column='dropping_time')
    car = models.ForeignKey(Car, related_name='cars')
    person = models.ForeignKey(Person, related_name='persons')
    created = models.DateTimeField(db_column='created_at', auto_now_add=True)

    class Meta:
        db_table = 'Car_Reservation'


class Customer_Care_Representative(models.Model):
    name = models.CharField(db_column='name', max_length=255)
    phone = models.CharField(db_column='phone', max_length=13)
    email = models.EmailField(db_column='email')
    image = models.ImageField(db_column='image', upload_to=upload_to)
    staff_type = models.CharField(db_column='type', choices=STAFF_CHOICES, default=VOICE_SUPPORT, max_length=25)
    created = models.DateTimeField(db_column='created', auto_now_add=True)
    is_active = models.BooleanField(db_column='is_active', default=True)

    class Meta:
        db_table = 'Customer_Care'


class Feedback(models.Model):
    first_name = models.CharField(db_column='first_name', max_length=255)
    last_name = models.CharField(db_column='last_name', max_length=255)
    phone = models.CharField(db_column='phone', max_length=13)
    email = models.EmailField(db_column='email')
    message = models.TextField(db_column='message')
    created = models.DateTimeField(db_column='created', auto_now_add=True)

    class Meta:
        db_table = 'Feedback'