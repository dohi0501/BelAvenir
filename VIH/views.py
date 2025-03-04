from django.shortcuts import render

# Create your views here.

def vih(request, *args, **kwargs):
    return render(request, 'vih.html')


def vih1(request, *args, **kwargs):
    return render(request, 'generalite_vih.html')


def cycle(request, *args, **kwargs):
    return render(request, 'cycle.html')