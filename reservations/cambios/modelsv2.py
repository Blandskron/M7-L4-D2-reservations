from django.db import models

class Reservation(models.Model):
    code = models.CharField(max_length=20, unique=True)

    # Renombrado semántico
    contact_name = models.CharField(
        max_length=120,
        db_comment="Nombre de contacto principal"
    )

    customer_email = models.EmailField()

    reservation_date = models.DateField(
        db_comment="Fecha efectiva de la reserva"
    )

    party_size = models.PositiveSmallIntegerField(default=1)

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("CONFIRMED", "Confirmed"),
        ("CANCELLED", "Cancelled"),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING",
        db_comment="Estado controlado de la reserva"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "reservation"
        ordering = ["reservation_date"]
        indexes = [
            models.Index(fields=["reservation_date"], name="idx_reservation_date"),
        ]