# Generated by Django 3.2.16 on 2022-11-14 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0020_auto_20221111_1819"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ticketuser",
            name="person",
        ),
        migrations.AddField(
            model_name="ticketuser",
            name="is_payed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="ticketuser",
            name="name",
            field=models.TextField(default=""),
        ),
    ]
