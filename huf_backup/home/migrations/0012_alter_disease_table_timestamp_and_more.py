# Generated by Django 4.1.7 on 2023-04-04 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0011_alter_disease_table_timestamp_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="disease_table",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 4, 12, 16, 42, 59490)
            ),
        ),
        migrations.AlterField(
            model_name="key_value_table",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 4, 12, 16, 42, 60402)
            ),
        ),
        migrations.AlterField(
            model_name="testimonial_table",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 4, 12, 16, 42, 59760)
            ),
        ),
        migrations.AlterField(
            model_name="video_table",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 4, 12, 16, 42, 60086)
            ),
        ),
    ]
