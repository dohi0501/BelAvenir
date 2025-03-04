from django.shortcuts import render

# Create your views here.
def accueil(request, *args, **kwargs):
    return render(request, 'index.html')

def generalite_vih(request, *args, **kwargs):
    return render(request, 'generalite_vih.html')

def cycle_vih(request, *args, **kwargs):
    return render(request, 'cycle_vih.html')

def reacton_corps_vih(request, *args, **kwargs):
    return render(request, 'reaction_corps.html')

def apres_infection_vih(request, *args, **kwargs):
    return render(request, 'apres_infection.html')
