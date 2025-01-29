from django import forms
from .models import Laboratorio

class LaboratorioFormCreate(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ["nombre", "ciudad", "pais"]

class LaboratorioFormUpdate(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ["nombre", "ciudad", "pais"]