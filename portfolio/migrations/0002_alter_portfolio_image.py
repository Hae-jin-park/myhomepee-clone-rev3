# Generated by Django 4.2.13 on 2024-06-27 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="portfolio",
            name="image",
            field=models.ImageField(upload_to="portfolio/%Y/%m/%d"),
        ),
    ]
