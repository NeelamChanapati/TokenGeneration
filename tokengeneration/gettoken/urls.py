from django.urls import path
from . import views

urlpatterns = [
    path('temp', views.temp, name='temp'),
    path('details', views.details_form, name='details_form'),
]