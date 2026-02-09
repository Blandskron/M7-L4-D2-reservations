from django.db import models

class Reservation(models.Model):
    code = models.CharField(max_length=20, unique=True)

    customer_name = models.CharField(max_length=120)

    # Nuevo campo requerido por operaciones
    customer_email = models.EmailField(
        db_comment="Email de contacto del cliente"
    )

    reservation_date = models.DateField()

    # Nuevo campo con valor por defecto
    party_size = models.PositiveSmallIntegerField(
        default=1,
        db_comment="Cantidad de personas asociadas a la reserva"
    )

    # Estado de la reserva
    status = models.CharField(
        max_length=20,
        default="PENDING",
        db_comment="Estado actual de la reserva"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "reservation"
        ordering = ["reservation_date"]