from django.urls import path
from .views import *

urlpatterns = [
    path('', depistage, name='depistage'),
]
