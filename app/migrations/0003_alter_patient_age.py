# Generated by Django 5.0.1 on 2024-01-24 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_dossiermedical_type_remove_medecin_specialty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.FloatField(max_length=3, null=True),
        ),
    ]
