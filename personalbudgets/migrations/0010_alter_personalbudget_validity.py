# Generated by Django 5.1 on 2024-09-29 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("personalbudgets", "0009_alter_personalbudget_validity_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personalbudget",
            name="validity",
            field=models.DateField(default="2024-09-29"),
        ),
    ]
