from django.contrib import admin

from reservations.models import (
    Reservation,
    Cleaner,
)

class ReservationAdmin(admin.ModelAdmin):
    pass

class CleanerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Cleaner, CleanerAdmin)
