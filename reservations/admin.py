from django.contrib import admin

from reservations.models import (
    Reservation,
    Cleaner,
    Address,
)

class ReservationAdmin(admin.ModelAdmin):
    pass

class CleanerAdmin(admin.ModelAdmin):
    pass

class AddressAdmin(admin.ModelAdmin):
    pass



admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Cleaner, CleanerAdmin)
admin.site.register(Address, AddressAdmin)
