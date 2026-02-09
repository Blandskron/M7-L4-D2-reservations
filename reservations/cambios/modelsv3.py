from django.db import models

class Reservation(models.Model):
    code = models.CharField(max_length=20, unique=True)

    contact_name = models.CharField(max_length=120)

    customer_email = models.EmailField(
        null=False,
        blank=False,
        db_comment="Email obligatorio para notificaciones"
    )

    reservation_date = models.DateField()

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
    )

    created_at = models.DateTimeField(auto_now_add=True)

    # Nuevo campo técnico
    updated_at = models.DateTimeField(
        auto_now=True,
        db_comment="Última modificación del registro"
    )

    class Meta:
        db_table = "reservation"
        ordering = ["reservation_date"]
        indexes = [
            models.Index(fields=["reservation_date"], name="idx_reservation_date"),
            models.Index(fields=["status"], name="idx_reservation_status"),
        ]