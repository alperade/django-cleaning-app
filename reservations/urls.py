from django.urls import path

from reservations.views import (
    ReservationListView,
    ReservationCreateView,
    ReservationDetailView,
    ReservationUpdateView,
    ReservationPickDateTimeView,
    ReservationDeleteView
)

urlpatterns = [
    path("", ReservationListView, name="home"),
    path("create/", ReservationCreateView, name="create_reservation"),
    path("<int:pk>/datetime", ReservationPickDateTimeView, name="datetime"),
    path("<int:pk>/updated/", ReservationUpdateView, name="updated"),
    path("<int:pk>/detail", ReservationDetailView, name="detail"),
    path("<int:pk>/delete/", ReservationDeleteView, name="reservation_delete"),
   ]
