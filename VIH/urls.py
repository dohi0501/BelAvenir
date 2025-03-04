from django.urls import path
from .views import *

urlpatterns = [
    path('', vih, name='vih'),
    path('vih/generalite_sur_le_vih/', vih1, name='vih1'),
    path('vih/cycle_du_vih/', cycle, name='cycle'),
]
