from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "contact_name",
        "reservation_date",
        "status",
        "party_size",
        "created_at",
    )
    list_filter = ("status", "reservation_date")
    search_fields = ("code", "contact_name", "customer_email")