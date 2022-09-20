from django.urls import path

from reservations.views import (
    ReservationListView,
    PastReservationListView,
    AddressCreateView,
    ReservationCreateView,
    NewReservationPickDateView,
    ReservationDetailView,
    ReservationDeleteView,
    ReservationDateUpdateView,
    ReservationPickDateView,
    ReservationTimeUpdateView,
    ReservationPickTimeView,
)

urlpatterns = [
    path("", ReservationListView, name="home"),
    path("past_res", PastReservationListView, name="past"),
    path("add_address/", AddressCreateView, name="add_address"),
    path("new_reservation/", ReservationCreateView, name="new_reservation"),
    path("pick_date/", NewReservationPickDateView, name="new_date_pick"),
    path("<int:pk>/detail", ReservationDetailView, name="detail"),
    path("<int:pk>/delete/", ReservationDeleteView, name="reservation_delete"),
    path("<int:pk>/update_date/", ReservationDateUpdateView, name="update_date"),
    path("<int:pk>/pick_date/", ReservationPickDateView, name="date_pick"),
    path("<int:pk>/update_time/", ReservationTimeUpdateView, name="update_time"),
    path("<int:pk>/pick_time/", ReservationPickTimeView, name="time_pick"),

   ]
