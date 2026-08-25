from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("reservations", "0001_initial")]
    operations = [
        migrations.AddField(model_name="reservation", name="customer_email", field=models.EmailField(db_comment="Email obligatorio para notificaciones", default="sin-correo@example.com", max_length=254)),
        migrations.AddField(model_name="reservation", name="party_size", field=models.PositiveSmallIntegerField(db_comment="Cantidad de personas asociadas", default=1)),
        migrations.AddField(model_name="reservation", name="status", field=models.CharField(default="PENDING", max_length=20)),
    ]
