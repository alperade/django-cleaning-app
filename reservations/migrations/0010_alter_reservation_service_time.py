# Generated by Django 4.1.1 on 2022-09-11 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservations", "0009_alter_reservation_service_time_delete_servicetime"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="service_time",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
