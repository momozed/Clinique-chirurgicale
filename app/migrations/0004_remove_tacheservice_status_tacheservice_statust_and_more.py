# Generated by Django 5.0.1 on 2024-01-24 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_patient_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tacheservice',
            name='status',
        ),
        migrations.AddField(
            model_name='tacheservice',
            name='statusT',
            field=models.CharField(choices=[('1', 'en cours'), ('2', 'terminé')], default='1', max_length=20),
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='status',
            field=models.CharField(choices=[('1', 'en attente'), ('2', 'confirmé')], default='1', max_length=20),
        ),
    ]