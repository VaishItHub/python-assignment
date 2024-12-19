# simulation/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.simulate_inserts, name='simulate_inserts'),
]

