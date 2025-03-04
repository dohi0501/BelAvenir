from django.shortcuts import render

# Create your views here.

def charge_virale(request):
    return render(request, 'chargevirale.html')