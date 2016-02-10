from django.shortcuts import render
from django.views.generic import View
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import list_route
import os
from django.core.exceptions import ObjectDoesNotExist

from Car_RentalApp.imports import *

from rest_framework import viewsets, permissions

# Create your views here.


def prepare_queryset(_model):
    return _model.objects.all()


class Person_ViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    serializer_class = Person_Serializer
    queryset = prepare_queryset(_model=Person)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    @list_route(methods=['POST',])
    def check_user(self, request, *args, **kwargs):
        try:
            _person = Person.objects.get(email=self.request.data['email'])
            person_serializer = Person_Serializer(_person)
            return Response(data=person_serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error": "no user with the given email address"}, status=status.HTTP_204_NO_CONTENT)


class Car_Reservation_ViewSet(viewsets.ModelViewSet):

    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    serializer_class = Car_Reservation_Serializer
    queryset = prepare_queryset(_model=Car_Reservation)

    def perform_create(self, serializer):
        car_id = self.request.data['car']
        _car = Car.objects.get(id=car_id)
        _person = Person.objects.get(email=self.request.data['person'])
        if serializer.is_valid():
            serializer.save(car=_car, person=_person)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class Car_ViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    serializer_class = Car_Serializer
    queryset = prepare_queryset(_model=Car)

    def perform_update(self, serializer):
        try:
            car = self.get_object()
            if bool(car.image) and os.path.isfile(car.image.url):
                os.remove(car.image.url)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Customer_Care_Representative_ViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    serializer_class = Customer_Care_Representative_Serializer
    queryset = prepare_queryset(_model=Customer_Care_Representative)


class FeedBack_ViewSet(viewsets.ModelViewSet):

    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    serializer_class = Feedback_Serializer
    queryset = prepare_queryset(_model=Feedback)


class Home(View):

    def get(self, request, *args, **kwargs):
        return render(request, template_name="Car_RentalApp/home.html")