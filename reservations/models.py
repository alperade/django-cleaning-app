from django.db import models
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL

class Reservation(models.Model):
    user = models.ForeignKey(USER_MODEL, related_name=("reservations"), on_delete=models.CASCADE)
    reserved_on = models.DateTimeField(auto_now_add=True)
    building_num = models.SmallIntegerField()
    street = models.CharField(max_length=100)
    apt_num = models.CharField(max_length=20)
    service_date = models.DateField()
    service_time = models.CharField(max_length=20)
    cleaner = models.ForeignKey("Cleaner",related_name="reservations",on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Cleaning for {self.user} on {self.service_date} at {self.service_time} by {self.cleaner}'

class Cleaner(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_num = models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
