# Generated by Django 4.2.13 on 2024-07-14 08:14

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_category_post_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=froala_editor.fields.FroalaField(),
        ),
    ]
