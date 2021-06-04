from django.shortcuts import render
# Librerias de Registro usuario
from django.contrib.auth.models import user
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
# ---------------------------------------------------

class RegistroUsuario(CreateView):
    model = user
    template_name = "usuario/registrar.html"
    form_class = UserCreationForm
    success_url = reverse_lazy(repisa)