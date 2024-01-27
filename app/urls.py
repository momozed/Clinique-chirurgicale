from django.urls import path
from . import views

urlpatterns = [  
    path('',views.index, name="index"),
    path('liste_patients/',views.liste_patients, name="liste_patients"),
    path('liste_medecins/',views.liste_medecins, name="liste_medecins"),
    path('liste_dossiers_medicaux/', views.liste_dossiers_medicaux, name='lst_dm'),
    path('liste_rendez_vous/', views.liste_rendez_vous, name='lst_rdv'),
    path('liste_tache_service/', views.liste_taches_service, name='lst_ts'),

    path('details_patient/<int:patientID>/',views.details_patient, name="details_p"),
    path('details_medecin/<int:medecinID>/',views.details_medecin, name="details_m"),
    path('details_dossier_medicale/<int:dossierID>/',views.details_dossier_medicale, name="details_d"),
    path('details_tache_service/<int:tacheID>/',views.details_tache_service, name="details_t"),

    path('creer_patient/',views.creer_patient, name="patn"),
    path('creer_medecin/',views.creer_medecin, name="med"),
    path('creer_tache_service/',views.creer_tache_service, name="ts"),
    path('creer_dossier_medical/',views.creer_dossier_medical, name="dm"),
    path('planifier_rendez_vous/', views.planifier_rendez_vous,name='rdv'),

    path('supprimer_patient/<int:patientID>/', views.Suppression_patient,name='spr_patn'),
    path('supprimer_medecin/<int:medecinID>/', views.Suppression_medecin,name='spr_med'),
    path('supprimer_rdv/<int:renderVousID>/', views.Suppression_rdv,name='spr_rdv'),
    path('supprimer_ts/<int:tacheID>/', views.Suppression_ts,name='spr_ts'),
    path('supprimer_dm/<int:dossierID>/', views.Suppression_dm,name='spr_dm'),

    path('modification_rdv/<int:renderVousID>', views.Modifier_rdv, name='maj_rdv'),
    path('modification_med/<int:medecinID>', views.Modifier_med, name='maj_med'),
    path('modification_patn/<int:patientID>', views.Modifier_patn, name='maj_patn'),
    path('modification_dm/<int:dossierID>', views.Modifier_dm, name='maj_dm'),
    path('modification_ts/<int:tacheID>', views.Modifier_ts, name='maj_ts'),
    
]

