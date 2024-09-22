# Generated by Django 4.2.10 on 2024-05-14 15:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0432_alter_fileupload_file_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hospitaldoctors",
            name="area",
            field=models.IntegerField(
                choices=[
                    (1, "General Medicine"),
                    (2, "Pulmonology"),
                    (3, "Intensivist"),
                    (4, "Pediatrician"),
                    (5, "Others"),
                    (6, "Anesthesiologist"),
                    (7, "Cardiac Surgeon"),
                    (8, "Cardiologist"),
                    (9, "Dentist"),
                    (10, "Dermatologist"),
                    (11, "Diabetologist"),
                    (12, "Emergency Medicine Physician"),
                    (13, "Endocrinologist"),
                    (14, "Family Physician"),
                    (15, "Gastroenterologist"),
                    (16, "General Surgeon"),
                    (17, "Geriatrician"),
                    (18, "Hematologist"),
                    (29, "Immunologist"),
                    (20, "Infectious Disease Specialist"),
                    (21, "MBBS doctor"),
                    (22, "Medical Officer"),
                    (23, "Nephrologist"),
                    (24, "Neuro Surgeon"),
                    (25, "Neurologist"),
                    (26, "Obstetrician and Gynecologist"),
                    (27, "Oncologist"),
                    (28, "Oncology Surgeon"),
                    (29, "Ophthalmologist"),
                    (30, "Oral and Maxillofacial Surgeon"),
                    (31, "Orthopedic"),
                    (32, "Orthopedic Surgeon"),
                    (33, "Otolaryngologist (ENT)"),
                    (34, "Palliative care Physician"),
                    (35, "Pathologist"),
                    (36, "Pediatric Surgeon"),
                    (37, "Physician"),
                    (38, "Plastic Surgeon"),
                    (39, "Psychiatrist"),
                    (40, "Pulmonologist"),
                    (41, "Radio technician"),
                    (42, "Radiologist"),
                    (43, "Rheumatologist"),
                    (44, "Sports Medicine Specialist"),
                    (45, "Thoraco-Vascular Surgeon"),
                    (46, "Transfusion Medicine Specialist"),
                    (47, "Urologist"),
                    (48, "Nurse"),
                ]
            ),
        ),
    ]
