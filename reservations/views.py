from django.http import JsonResponse
from django.shortcuts import render

from .models import Reservation


def classroom(request):
    return render(request, "reservations/classroom.html")


def reservation_snapshot(request):
    data = list(Reservation.objects.values("code", "contact_name", "reservation_date", "status", "party_size"))
    return JsonResponse({"reservations": data})
