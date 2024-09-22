# Generated by Django 4.2.8 on 2024-05-28 05:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0438_alter_dailyround_patient_category_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalpatientregistration",
            name="ration_card_category",
            field=models.CharField(
                choices=[
                    ("NO_CARD", "Non-card holder"),
                    ("BPL", "BPL"),
                    ("APL", "APL"),
                ],
                max_length=8,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="patientregistration",
            name="ration_card_category",
            field=models.CharField(
                choices=[
                    ("NO_CARD", "Non-card holder"),
                    ("BPL", "BPL"),
                    ("APL", "APL"),
                ],
                max_length=8,
                null=True,
            ),
        ),
    ]
