from rest_framework import serializers
from Car_RentalApp.imports import *


class Person_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'phone', 'age', 'email', 'address', 'city', 'zip_code',]


class Car_Serializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=False)

    class Meta:
        model = Car
        fields = ['id', 'name', 'rent', 'model', 'doors', 'seats', 'luggage', 'air_condition', 'minimum_age', 'image', ]


class Car_Reservation_Serializer(serializers.ModelSerializer):
    car = serializers.PrimaryKeyRelatedField(source='car.name', read_only=True)
    person = serializers.PrimaryKeyRelatedField(source='person.email', read_only=True)
    pick_up_time = serializers.DateTimeField(input_formats=['%m/%d/%Y %I:%M %p'])
    dropping_time = serializers.DateTimeField(input_formats=['%m/%d/%Y %I:%M %p'])

    class Meta:
        model = Car_Reservation
        fields = ['id', 'source', 'destination', 'pick_up_time', 'dropping_time', 'car', 'person', ]


class Customer_Care_Representative_Serializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=False)

    class Meta:
        model = Customer_Care_Representative
        fields = ['name', 'phone', 'email', 'image', 'staff_type', ]


class Feedback_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = ['first_name', 'last_name', 'phone', 'email', 'message', ]
