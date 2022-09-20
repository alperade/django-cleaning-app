from django import forms

from reservations.models import Reservation, Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["building_num", "street", "apt_num"]

class ReservationDeleteForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = []


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["service_date_time"]
