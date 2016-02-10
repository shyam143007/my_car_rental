from django.conf.urls import url, patterns, include

from rest_framework.routers import DefaultRouter

from Car_RentalApp import views

car_rental_router = DefaultRouter()
car_rental_router.register(prefix='person', viewset=views.Person_ViewSet)
car_rental_router.register(prefix='car_reservation', viewset=views.Car_Reservation_ViewSet)
car_rental_router.register(prefix='car', viewset=views.Car_ViewSet)
car_rental_router.register(prefix='feedback', viewset=views.FeedBack_ViewSet)
car_rental_router.register(prefix='customer_care', viewset=views.Customer_Care_Representative_ViewSet)


urlpatterns = [
    url('api_review/', include(car_rental_router.urls)),
    url('', view=views.Home.as_view()),
]