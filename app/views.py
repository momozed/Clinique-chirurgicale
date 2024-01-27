from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .models import Patient, Medecin, RendezVous, DossierMedical, TacheService
from .forms import PatientForm,RendezVousForm, MedecinForm, TacheServiceForm, DossierMedicalForm


def index(request):
    return render(request, 'index.html', )

def liste_patients(request):
    patients = Patient.objects.all()
    return render(request, 'liste_patients.html', {'patients': patients})

def liste_medecins(request):
    medecins = Medecin.objects.all()
    return render(request, 'liste_medecins.html', {'medecins': medecins})

def liste_dossiers_medicaux(request):
    dossiers_medicaux = DossierMedical.objects.all()
    return render(request, 'liste_dossiers_medicaux.html', {'dossiers_medicaux': dossiers_medicaux})

def liste_taches_service(request):
    taches_service = TacheService.objects.all()
    return render(request, 'liste_tache_service.html', {'taches_service': taches_service})

def liste_rendez_vous(request):
    rendez_vous = RendezVous.objects.all()
    return render(request, 'liste_rendez_vous.html', {'rendez_vous': rendez_vous})



def details_patient(request, patientID):
    patient = get_object_or_404(Patient, patientID=patientID)
    return render(request, 'details_patient.html', {'patient': patient})

def details_medecin(request, medecinID):
    medecin = get_object_or_404(Medecin, medecinID=medecinID)
    return render(request, 'details_medecin.html', {'medecin': medecin})

def details_dossier_medicale(request, dossierID):
    dossier = get_object_or_404(DossierMedical, dossierID=dossierID)
    return render(request, 'details_dossier_medicale.html', {'dossier': dossier})

def details_tache_service(request, tacheID):
    tache = get_object_or_404(TacheService, tacheID=tacheID)
    return render(request, 'details_tache_service.html', {'tache': tache})



def creer_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_patients')
    else:
        form = PatientForm()
    return render(request, 'creer_patient.html', {'form': form})

def creer_medecin(request):
    if request.method == 'POST':
        form = MedecinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_medecins')
    else:
        form = MedecinForm()
    return render(request, 'creer_medecin.html', {'form': form})

def creer_tache_service(request):
    if request.method == 'POST':
        form = TacheServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lst_ts')
    else:
        form = TacheServiceForm()
    return render(request, 'creer_tache_service.html', {'form': form})

def creer_dossier_medical(request):
    if request.method == 'POST':
        form = DossierMedicalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lst_dm')
    else:
        form = DossierMedicalForm()
    return render(request, 'creer_dossier_medicale.html', {'form': form})

def planifier_rendez_vous(request):
    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lst_rdv')
    else:
        form = RendezVousForm()
    return render(request, 'planifier_rendez_vous.html', {'form': form})



def Suppression_patient(request, patientID) :
    patient = get_object_or_404(Patient, patientID=patientID)
    if request.method == 'POST' :
        patient.delete()
        return redirect('liste_patients')
    return render (request,  {'patient' : patient})

def Suppression_medecin(request, medecinID) :
    medecin = get_object_or_404(Medecin, medecinID=medecinID)
    if request.method == 'POST' :
        medecin.delete()
        return redirect('liste_medecins')
    return render (request,  {'medecin' : medecin})

def Suppression_rdv(request, renderVousID) :
    rdv = get_object_or_404(RendezVous, renderVousID=renderVousID)
    if request.method == 'POST' :
        rdv.delete()
        return redirect('lst_rdv')
    return render (request,  {'rdv' : rdv})

def Suppression_ts(request, tacheID) :
    ts = get_object_or_404(TacheService, tacheID=tacheID)
    if request.method == 'POST' :
        ts.delete()
        return redirect('lst_ts')
    return render (request,  {'ts' : ts})

def Suppression_dm(request, dossierID) :
    dm = get_object_or_404(DossierMedical, dossierID=dossierID)
    if request.method == 'POST' :
        dm.delete()
        return redirect('lst_dm')
    return render (request,   {'dm' : dm})



def Modifier_rdv(request, renderVousID):
    rdv = get_object_or_404(RendezVous, renderVousID=renderVousID)
    if request.method == 'POST':
        form = RendezVousForm(request.POST, instance=rdv)
        if form.is_valid():
             # mettre à jour l’objet dans la base de données
             form.save()
             # rediriger vers la page liste commandes
             return redirect('lst_rdv')  
        else :
            form = RendezVousForm(instance=rdv)
            return render(request, 'rdv_update.html',{'form' : form} ) 
    else :
        form = RendezVousForm(instance=rdv)
        # on pré-remplir le formulaire avec l’objet ayant l’id spécifié
        return render(request, 'rdv_update.html',{'form' : form} )
    
def Modifier_med(request, medecinID):
    med = get_object_or_404(Medecin, medecinID=medecinID)
    if request.method == 'POST':
        form = MedecinForm(request.POST, instance=med)
        if form.is_valid():
             # mettre à jour l’objet dans la base de données
             form.save()
             # rediriger vers la page liste commandes
             return redirect('liste_medecins')  
        else :
            form = MedecinForm(instance=med)
            return render(request, 'med_update.html',{'form' : form} ) 
    else :
        form = MedecinForm(instance=med)
        # on pré-remplir le formulaire avec l’objet ayant l’id spécifié
        return render(request, 'med_update.html',{'form' : form} )
    
def Modifier_patn(request, patientID):
    patn = get_object_or_404(Patient, patientID=patientID)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patn)
        if form.is_valid():
             # mettre à jour l’objet dans la base de données
             form.save()
             # rediriger vers la page liste commandes
             return redirect('liste_patients')  
        else :
            form = PatientForm(instance=patn)
            return render(request, 'patn_update.html',{'form' : form} ) 
    else :
        form = PatientForm(instance=patn)
        # on pré-remplir le formulaire avec l’objet ayant l’id spécifié
        return render(request, 'patn_update.html',{'form' : form} )
    
def Modifier_dm(request, dossierID):
    dm = get_object_or_404(DossierMedical, dossierID=dossierID)
    if request.method == 'POST':
        form = DossierMedicalForm(request.POST, instance=dm)
        if form.is_valid():
             # mettre à jour l’objet dans la base de données
             form.save()
             # rediriger vers la page liste commandes
             return redirect('lst_dm')  
        else :
            form = DossierMedicalForm(instance=dm)
            return render(request, 'dm_update.html',{'form' : form} ) 
    else :
        form = DossierMedicalForm(instance=dm)
        # on pré-remplir le formulaire avec l’objet ayant l’id spécifié
        return render(request, 'dm_update.html',{'form' : form} )

def Modifier_ts(request, tacheID):
    ts = get_object_or_404(TacheService, tacheID=tacheID)
    if request.method == 'POST':
        form = TacheServiceForm(request.POST, instance=ts)
        if form.is_valid():
             # mettre à jour l’objet dans la base de données
             form.save()
             # rediriger vers la page liste commandes
             return redirect('lst_ts')  
        else :
            form = TacheServiceForm(instance=ts)
            return render(request, 'ts_update.html',{'form' : form} ) 
    else :
        form = TacheServiceForm(instance=ts)
        # on pré-remplir le formulaire avec l’objet ayant l’id spécifié
        return render(request, 'ts_update.html',{'form' : form} )
        