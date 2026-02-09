from django.db import models

class Reservation(models.Model):
    # Identificador público de la reserva
    code = models.CharField(
        max_length=20,
        unique=True,
        db_comment="Código público de la reserva"
    )

    # Nombre de quien realiza la reserva
    customer_name = models.CharField(
        max_length=120,
        db_comment="Nombre del cliente"
    )

    # Fecha reservada
    reservation_date = models.DateField(
        db_comment="Fecha principal de la reserva"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_comment="Momento de creación de la reserva"
    )

    class Meta:
        db_table = "reservation"
        ordering = ["reservation_date"]