# Generated by Django 4.1.1 on 2022-09-15 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservations", "0011_time"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reservation",
            name="service_date",
        ),
        migrations.AddField(
            model_name="reservation",
            name="service_date_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]