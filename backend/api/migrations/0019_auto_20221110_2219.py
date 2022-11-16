# Generated by Django 3.2.16 on 2022-11-10 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0018_alter_event_tickets"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="tickets",
        ),
        migrations.AddField(
            model_name="event",
            name="ticketEnd",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="ticketLimit",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="ticketStart",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name="EventTicket",
        ),
    ]
