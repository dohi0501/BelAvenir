from django.shortcuts import render

# Create your views here.

def depistage(request, *args, **kwargs):
    return render(request, 'depistage.html')
