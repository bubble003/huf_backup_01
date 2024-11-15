# Generated by Django 4.1.7 on 2023-09-19 16:06

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0019_historicalvideo_table_historicaltestimonial_table_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicaltestimonial_table",
            name="heading",
            field=models.CharField(
                max_length=100, validators=[home.models.validate_small_letters]
            ),
        ),
        migrations.AlterField(
            model_name="historicaltestimonial_table",
            name="name",
            field=models.CharField(
                max_length=50, validators=[home.models.validate_small_letters]
            ),
        ),
        migrations.AlterField(
            model_name="historicalvideo_table",
            name="image",
            field=models.TextField(
                max_length=100, validators=[home.models.validate_webp_image]
            ),
        ),
        migrations.AlterField(
            model_name="testimonial_table",
            name="heading",
            field=models.CharField(
                max_length=100, validators=[home.models.validate_small_letters]
            ),
        ),
        migrations.AlterField(
            model_name="testimonial_table",
            name="name",
            field=models.CharField(
                max_length=50, validators=[home.models.validate_small_letters]
            ),
        ),
        migrations.AlterField(
            model_name="video_table",
            name="image",
            field=models.ImageField(
                upload_to="video_table_images/",
                validators=[home.models.validate_webp_image],
            ),
        ),
    ]
