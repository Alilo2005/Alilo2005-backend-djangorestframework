# Generated by Django 5.1.4 on 2024-12-29 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="published_date",
            field=models.DateField(),
        ),
    ]
