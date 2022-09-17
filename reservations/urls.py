from django.urls import path

from reservations.views import (
    ReservationListView,
    ReservationCreateView,
    ReservationDetailView,
    ReservationDeleteView,
    ReservationDateUpdateView,
    ReservationPickDateView,
    ReservationTimeUpdateView,
    ReservationPickTimeView,
)

urlpatterns = [
    path("", ReservationListView, name="home"),
    path("create/", ReservationCreateView, name="create_reservation"),
    path("<int:pk>/detail", ReservationDetailView, name="detail"),
    path("<int:pk>/delete/", ReservationDeleteView, name="reservation_delete"),
    path("<int:pk>/update_date/", ReservationDateUpdateView, name="update_date"),
    path("<int:pk>/pick_date/", ReservationPickDateView, name="date_pick"),
    path("<int:pk>/update_time/", ReservationTimeUpdateView, name="update_time"),
    path("<int:pk>/pick_time/", ReservationPickTimeView, name="time_pick"),

   ]
