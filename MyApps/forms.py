from django import forms
from django.forms import modelformset_factory
from .models import *

class FormRapprt(forms.ModelForm):
    date_debut = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )
    date_fin = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )
    lieu = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Lieu de la formation'}),
        required=False
    )
    titre = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Titre de la formation'}),
        required=True
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Description sur la formation', 'rows': 4, 'cols': 50}),
        required=False
    )
    class Meta:
        model = RapportFormation
        fields = ['date_debut', 'date_fin', 'lieu', 'titre', 'description', 'pdf_recapitulatif', 'img_formation']


class FormImage(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Description sur la formation', 'rows': 4, 'cols': 50})
    )
    class Meta:
        model = ImageRapport
        fields = ['rapport' ,'image', 'description']


class FormVideo(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Description sur la formation', 'rows': 4, 'cols': 50})
    )
    class Meta:
        model = VideosRapport
        fields = ['rapport' ,'video', 'description']