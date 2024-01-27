from django import forms
from .models import RendezVous, Patient, Medecin,TacheService, DossierMedical

class RendezVousForm(forms.ModelForm):
    class Meta:
        model = RendezVous
        fields = '__all__'

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class MedecinForm(forms.ModelForm):
    class Meta:
        model = Medecin
        fields = '__all__'

class DossierMedicalForm(forms.ModelForm):
    class Meta:
        model = DossierMedical
        fields = '__all__'

class TacheServiceForm(forms.ModelForm):
    class Meta:
        model = TacheService
        fields = '__all__'