from django.contrib import admin
from .models import (
    Vehicle, VehicleDetails, Location, Booking,
    VehicleStatistics, BookingDetails, TerminateBooking
)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    model = Vehicle
    list_display = ("model_manufacturer", "model_name", "vehicle_owner")


admin.site.register(VehicleDetails)
admin.site.register(Location)
admin.site.register(Booking)
admin.site.register(VehicleStatistics)
admin.site.register(BookingDetails)
admin.site.register(TerminateBooking)
