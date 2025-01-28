from django.urls import path
from laboratorio.views import *
from . import views

urlpatterns = [
    path('', index, name='index'),
]