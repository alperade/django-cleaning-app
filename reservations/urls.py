from django.urls import path

from reservations.views import (
    ReservationListView,
    ReservationCreateView,
)

urlpatterns = [
    path("", ReservationListView, name="home"),
    path("create/", ReservationCreateView, name="create_reservation"),
   ]
