# Generated by Django 4.2.7 on 2023-11-22 16:45

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=255, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=255, verbose_name="Last Name"),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="Email"
                    ),
                ),
                ("password", models.CharField(max_length=255)),
                ("date_of_birth", models.DateField(verbose_name="Date of Birth")),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region="IN", unique=True
                    ),
                ),
                (
                    "is_manager",
                    models.BooleanField(default=False, verbose_name="Is Manager"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
