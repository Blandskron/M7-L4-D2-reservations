from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("reservations", "0003_rename_and_constraints")]
    operations = [
        migrations.AddField(model_name="reservation", name="updated_at", field=models.DateTimeField(auto_now=True, db_comment="Última modificación")),
        migrations.AddIndex(model_name="reservation", index=models.Index(fields=["status"], name="idx_reservation_status")),
        migrations.AddConstraint(model_name="reservation", constraint=models.CheckConstraint(condition=models.Q(("party_size__gte", 1)), name="reservation_party_size_gte_1")),
    ]
