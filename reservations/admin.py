from django.contrib import admin

from reservations.models import (
    Reservation,
    Cleaner,
    Time,
)

class ReservationAdmin(admin.ModelAdmin):
    pass

class CleanerAdmin(admin.ModelAdmin):
    pass

class TimeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Cleaner, CleanerAdmin)
admin.site.register(Time, TimeAdmin)
