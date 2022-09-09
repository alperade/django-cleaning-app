from django.contrib import admin

from reservations.models import (
    Reservation,
    Cleaner,
    ServiceTime,
)

class ReservationAdmin(admin.ModelAdmin):
    pass

class CleanerAdmin(admin.ModelAdmin):
    pass

class ServiceTimeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Cleaner, CleanerAdmin)
admin.site.register(ServiceTime, ServiceTimeAdmin)
