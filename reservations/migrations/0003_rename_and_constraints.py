from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("reservations", "0002_add_contact_and_status")]
    operations = [
        migrations.RenameField(model_name="reservation", old_name="customer_name", new_name="contact_name"),
        migrations.AlterField(model_name="reservation", name="contact_name", field=models.CharField(db_comment="Nombre de contacto principal", max_length=120)),
        migrations.AlterField(model_name="reservation", name="reservation_date", field=models.DateField(db_comment="Fecha efectiva de la reserva")),
        migrations.AlterField(model_name="reservation", name="status", field=models.CharField(choices=[("PENDING", "Pendiente"), ("CONFIRMED", "Confirmada"), ("CANCELLED", "Cancelada")], db_comment="Estado controlado", default="PENDING", max_length=20)),
        migrations.AddIndex(model_name="reservation", index=models.Index(fields=["reservation_date"], name="idx_reservation_date")),
    ]
