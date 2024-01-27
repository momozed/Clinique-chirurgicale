import datetime
from django.db import models
from django.contrib.auth.models import User

STATUE_CHOICES = ( 
    ("en attente", "en attente"), 
    ("confirmé", "confirmé"), 
) 

STATUET_CHOICES = ( 
    ("en cours", "en cours"), 
    ("terminé", "terminé"), 
) 


class Patient(models.Model):
    patientID= models.CharField(primary_key=True,max_length=20, unique=True)
    first_name= models.CharField(max_length = 50, null = True)
    last_name= models.CharField(max_length = 50, null = True)
    age = models.PositiveSmallIntegerField( null = True)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    def __str__(self):
         return self.last_name

class Medecin(models.Model):
    medecinID= models.CharField(primary_key=True,max_length=20, unique=True)
    first_name= models.CharField(max_length = 50, null = True)
    last_name= models.CharField(max_length = 50, null = True)
    phone_number = models.CharField(max_length=20)
    def __str__(self):
         return self.last_name

class RendezVous(models.Model):
    renderVousID= models.CharField(primary_key=True,max_length=20, unique=True)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices = STATUE_CHOICES, default = 'en attente')  # confirmé, en attente
    created_at = models.DateTimeField(default=datetime.datetime.now)
    patientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecinID = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    def __str__(self):
         return self.renderVousID

class DossierMedical(models.Model):
    dossierID= models.CharField(primary_key=True,max_length=20, unique=True)
    medical_info = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now)
    patientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    rendezvousID = models.ForeignKey(RendezVous, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
         return self.dossierID


class TacheService(models.Model):
    tacheID= models.CharField(primary_key=True,max_length=20, unique=True)
    description = models.TextField()
    statusT = models.CharField(max_length=20, choices = STATUET_CHOICES, default = 'en cours')  # en cours, terminé
    deadline = models.DateField()
    medecinID = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    rendezvousID = models.ForeignKey(RendezVous, on_delete=models.CASCADE, null=True)
    def __str__(self):
         return self.tacheID

