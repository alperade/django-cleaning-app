# Generated by Django 4.1.1 on 2022-09-09 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reservations", "0007_alter_servicetime_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="service_time",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reservations",
                to="reservations.servicetime",
            ),
        ),
        migrations.AlterField(
            model_name="servicetime",
            name="time",
            field=models.CharField(
                blank=True,
                choices=[("9AM", "9AM"), ("10AM", "10AM"), ("11AM", "11AM")],
                max_length=20,
                null=True,
            ),
        ),
    ]
