from django.shortcuts import render, redirect 
from .forms import ContactoModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth import login, logout 
from django.contrib.auth.forms import AuthenticationForm 




def inicio(request):
    return render(request, 'principal/inicio.html')

@login_required 
def contacto(request):
    if request.method == "POST":
        form = ContactoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "principal/contacto_exito.html")
    else:
        form = ContactoModelForm()

    return render(request, "principal/contacto.html", {"form": form})

class PanelAdminView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = "principal/admin_panel.html"
    permission_required = "principal.view_consultacontacto"
    
from .forms import RegistroForm

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            login(request, user)
            return redirect("inicio")
    else:
        form = RegistroForm()

    return render(request, "principal/registro.html", {"form": form})