from django.http import JsonResponse
from .models import Reservation

def reservation_snapshot(request):
    data = list(
        Reservation.objects.values(
            "code",
            "contact_name",
            "reservation_date",
            "status",
            "party_size"
        )
    )
    return JsonResponse({"reservations": data})