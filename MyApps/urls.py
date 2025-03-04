from django.urls import path
from .views import *

urlpatterns = [
    # root pour la page d'accueil
    path('', accueil, name='accueil'),
    #  root pour le vih
    path('vih/generalite_vih/', generalite_vih, name='generalite_vih'),
    path('vih/cycle_de_vie_vih/', cycle_vih, name='cycle_vih'),
    path('vih/reaction_du_corps/', reacton_corps_vih, name='reacton_corps_vih'),
    path('vih/apres_infection_vih/', apres_infection_vih, name='apres_infection_vih'),
    # root pour les ist
    
]