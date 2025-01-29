from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Laboratorio
from .forms import LaboratorioFormCreate, LaboratorioFormUpdate

# Create your views here.
def index(request):
    return render(request, 'index.html')


#CREATE LABS
def laboratorio_create(request):
    if request.method == "POST":
        form = LaboratorioFormCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("laboratorio_list"))
    else:
        form = LaboratorioFormCreate()
    return render(request, "laboratorio/laboratorio_form_create.html", {"form": form})


#READ LABS (LISTAR)
def laboratorio_list(request):
    laboratorios = Laboratorio.objects.all().order_by("id")
    return render(request, "laboratorio/laboratorio_list.html", {"laboratorios": laboratorios})


#UPDATE LABS
def laboratorio_update(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == "POST":
        form = LaboratorioFormUpdate(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect(reverse("laboratorio_list"))
    else:
        form = LaboratorioFormUpdate(instance=laboratorio)
    return render(request, "laboratorio/laboratorio_form_update.html", {"form": form})


#DELETE LABS
def laboratorio_delete(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == "POST":
        laboratorio.delete()
        return redirect(reverse("laboratorio_list"))
    return render(request, "laboratorio/laboratorio_confirm_delete.html", {"laboratorio": laboratorio})
