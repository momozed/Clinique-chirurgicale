# Generated by Django 5.0.1 on 2024-01-25 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rendezvous_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dossiermedical',
            old_name='patient',
            new_name='patientID',
        ),
        migrations.RenameField(
            model_name='dossiermedical',
            old_name='rendezvous',
            new_name='rendezvousID',
        ),
        migrations.RenameField(
            model_name='rendezvous',
            old_name='medecin',
            new_name='medecinID',
        ),
        migrations.RenameField(
            model_name='rendezvous',
            old_name='patient',
            new_name='patientID',
        ),
        migrations.RenameField(
            model_name='tacheservice',
            old_name='medecin',
            new_name='medecinID',
        ),
        migrations.RenameField(
            model_name='tacheservice',
            old_name='rendezvous',
            new_name='rendezvousID',
        ),
    ]
