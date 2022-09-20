# Generated by Django 4.1.1 on 2022-09-20 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("reservations", "0013_delete_time"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reservation",
            name="apt_num",
        ),
        migrations.RemoveField(
            model_name="reservation",
            name="building_num",
        ),
        migrations.RemoveField(
            model_name="reservation",
            name="street",
        ),
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("building_num", models.SmallIntegerField()),
                ("street", models.CharField(max_length=100)),
                ("apt_num", models.CharField(max_length=20)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="addresses",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="reservation",
            name="address",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="reservations",
                to="reservations.address",
            ),
        ),
    ]
