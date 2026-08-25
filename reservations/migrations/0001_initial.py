from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Reservation",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code", models.CharField(db_comment="Código público de la reserva", max_length=20, unique=True)),
                ("customer_name", models.CharField(max_length=120)),
                ("reservation_date", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True, db_comment="Momento de creación")),
            ],
            options={"db_table": "reservation", "ordering": ["reservation_date"]},
        )
    ]
