# Generated by Django 4.2.7 on 2023-11-18 13:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_maillogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maillogs',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 18, 13, 35, 15, 786099, tzinfo=datetime.timezone.utc)),
        ),
    ]
