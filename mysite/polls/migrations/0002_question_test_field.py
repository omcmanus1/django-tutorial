# Generated by Django 5.0.6 on 2024-07-08 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="test_field",
            field=models.CharField(default="", max_length=100),
        ),
    ]
