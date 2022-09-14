from django.urls import path

from reservations.views import (
    ReservationListView,
    ReservationCreateView,
    ReservationDetailView,
    ReservationUpdateView,
)

urlpatterns = [
    path("", ReservationListView, name="home"),
    path("create/", ReservationCreateView, name="create_reservation"),
    path("<int:pk>/detail", ReservationDetailView, name="detail"),
    path("<int:pk>/updated/", ReservationUpdateView, name="updated"),

   ]
