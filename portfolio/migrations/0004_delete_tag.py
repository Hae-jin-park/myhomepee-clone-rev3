# Generated by Django 4.2.13 on 2024-06-28 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0003_remove_portfolio_tag_set"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Tag",
        ),
    ]
