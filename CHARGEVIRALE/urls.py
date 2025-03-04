from django.urls import path
from .views import *

urlpatterns = [
    path('', charge_virale, name='charge_virale'),
]
