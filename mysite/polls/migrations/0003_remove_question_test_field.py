# Generated by Django 5.0.6 on 2024-07-11 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0002_question_test_field"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="question",
            name="test_field",
        ),
    ]
