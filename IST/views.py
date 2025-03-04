from django.shortcuts import render

# Create your views here.

def ist(request, *args, **kwargs):
    return render(request, 'ist.html')