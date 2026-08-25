from django.db import models


class Reservation(models.Model):
    """Modelo final del aula, resultado de cuatro migraciones incrementales."""

    code = models.CharField(max_length=20, unique=True, db_comment="Código público de la reserva")
    contact_name = models.CharField(max_length=120, db_comment="Nombre de contacto principal")
    customer_email = models.EmailField(db_comment="Email obligatorio para notificaciones")
    reservation_date = models.DateField(db_comment="Fecha efectiva de la reserva")
    party_size = models.PositiveSmallIntegerField(default=1, db_comment="Cantidad de personas asociadas")

    STATUS_CHOICES = [
        ("PENDING", "Pendiente"),
        ("CONFIRMED", "Confirmada"),
        ("CANCELLED", "Cancelada"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING", db_comment="Estado controlado")
    created_at = models.DateTimeField(auto_now_add=True, db_comment="Momento de creación")
    updated_at = models.DateTimeField(auto_now=True, db_comment="Última modificación")

    class Meta:
        db_table = "reservation"
        ordering = ["reservation_date"]
        indexes = [
            models.Index(fields=["reservation_date"], name="idx_reservation_date"),
            models.Index(fields=["status"], name="idx_reservation_status"),
        ]
        constraints = [
            models.CheckConstraint(condition=models.Q(party_size__gte=1), name="reservation_party_size_gte_1")
        ]
