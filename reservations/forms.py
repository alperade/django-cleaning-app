from django import forms

from reservations.models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["building_num", "street", "apt_num"]

class ReservationDeleteForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = []
