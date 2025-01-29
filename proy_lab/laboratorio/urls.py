from django.urls import path
from laboratorio.views import *
from . import views

urlpatterns = [
    path('', index, name='index'),
    path("laboratorios/", laboratorio_list, name="laboratorio_list"),
    path('laboratorios/crear/', laboratorio_create, name='laboratorio_create'),
    path("laboratorios/editar/<int:pk>/", laboratorio_update, name="laboratorio_update"),
    path("laboratorios/eliminar/<int:pk>/", laboratorio_delete, name="laboratorio_delete"),
]
