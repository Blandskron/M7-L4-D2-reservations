from django.contrib import admin
from django.urls import path

from reservations.views import classroom, reservation_snapshot


urlpatterns = [
    path('', classroom, name='classroom'),
    path('admin/', admin.site.urls),
    path('api/reservations/', reservation_snapshot, name='reservation-snapshot'),
]
