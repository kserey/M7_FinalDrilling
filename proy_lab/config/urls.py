from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from django.views import *
from laboratorio.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('laboratorio/', include('laboratorio.urls')),
]
