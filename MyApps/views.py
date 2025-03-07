from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import user_passes_test, login_required

# Create your views here.

# identification
def is_admin(user):
    return user.is_authenticated and user.is_staff and user.is_superuser


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

def generalite_ist(request, *args, **kwargs):
    return render(request, 'generalite_ist.html')

def apropos(request, *args, **kwargs):
    return render(request, 'apropos.html')

def projets(request, *args, **kwargs):
    return render(request, 'projets.html')

# Administration 
def login_admin(request, *args, **kwargs):
    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                try:
                    login(request, user)
                    return redirect('administration', username=username)
                
                except:
                    erreur = 'une erreur est survenue!'
                    return render(request, 'login_administration.html', {'form': form, 'error': erreur})

            
            else:
                erreur = 'une erreur est survenue!'
                return render(request, 'login_administration.html', {'form': form, 'error': erreur})
        
        else:
            erreur = 'nom ou mot de passe invalide!'
            return render(request, 'login_administration.html', {'form': form, 'error': erreur})

    else:
        form = AuthenticationForm()
        return render(request, 'login_administration.html', {'form': form})
    


@login_required(login_url='login_Administration/')
@user_passes_test(is_admin)
def administration (request, username, *args, **kwargs):
    user = User.objects.get(username=username)
    return render(request, 'administration.html', {'user': user})


@login_required(login_url='login_Administration/')
@user_passes_test(is_admin)
def logout_user (request, *args, **kwargs):
    logout(request)
    return redirect('accueil')

