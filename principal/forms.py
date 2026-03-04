from django import forms
from django.contrib.auth.models import User
from .models import ConsultaContacto


# FORMULARIO DE CONTACTO (MODELFORM)
class ContactoModelForm(forms.ModelForm):
    class Meta:
        model = ConsultaContacto
        fields = ["nombre", "correo", "mensaje"]


# FORMULARIO DE REGISTRO
class RegistroForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["username", "email"]

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password1") != cleaned_data.get("password2"):
            self.add_error("password2", "Las contraseñas no coinciden")
        return cleaned_data