# Generated by Django 4.2.7 on 2023-11-20 05:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_maillogs_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maillogs',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 20, 5, 47, 53, 813249, tzinfo=datetime.timezone.utc)),
        ),
    ]