# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, FormView
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail, EmailMessage
from .models import Categoria
from muebles.models import Mueble
from .forms import ContactForm


# CLASE PARA DESPLEGAR LOS COMEDORES EN LISTA
class ComedoresListView(ListView):
    model = Mueble
    template_name = "ComedoresCategoryTemplateView.html"
    paginate_by = 4
    ordering = ["id"]

    def get_queryset(self):
        queryset = super(ComedoresListView, self).get_queryset()
        return queryset.filter(categoria__cat_mueble="comedores")


# CLASE PARA DESPLEGAR LOS COCINAS EN LISTA
class CocinasListView(ListView):
    model = Mueble
    template_name = "CocinasCategoryTemplateView.html"
    paginate_by = 4
    ordering = ["id"]

    def get_queryset(self):
        queryset = super(CocinasListView, self).get_queryset()
        return queryset.filter(categoria__cat_mueble="cocinas")


# CLASE PARA DESPLEGAR LOS CHIFONIERS EN LISTA
class ChifoniersListView(ListView):
    model = Mueble
    template_name = "ChifoniersCategoryTemplateView.html"
    paginate_by = 4
    ordering = ["id"]

    def get_queryset(self):
        queryset = super(ChifoniersListView, self).get_queryset()
        return queryset.filter(categoria__cat_mueble="chifoniers")


# CLASE PARA DESPLEGAR LOS CUNAS EN LISTA
class CunasListView(ListView):
    model = Mueble
    template_name = "CunasCategoryTemplateView.html"
    paginate_by = 4
    ordering = ["id"]

    def get_queryset(self):
        queryset = super(CunasListView, self).get_queryset()
        return queryset.filter(categoria__cat_mueble="cunas")


# CLASE PARA EL FORMULARIO DE CONTACTO, MANDA MAIL POR MEDIO DE GMAIL, NO SE OCUPA UN MODELO PARA GUARDARLO EN BD
class ContactFormView(FormView):
    template_name = 'ContactTemplateView.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """
        message = "{subject} / {sender} envio el siguiente comentario: ".format(
            sender=form.cleaned_data['sender'],
            subject=form.cleaned_data['subject']
        )
        """
        sender = form.cleaned_data['sender']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']

        """message += "\n\n{0}".format(form.cleaned_data['message'])"""
        body = "Titulo: " + subject + "\n"
        + "Envia: " + sender + "\n"
        + "Mensaje: " + message
        recipients = ['rodolfougaldeochoa@gmail.com']

        mail = EmailMessage(subject, body, sender, recipients, reply_to=['noreply@gmail.com'])
        mail.send()

        return super(ContactFormView, self). form_valid(form)

        """email = EmailMessage('Hello', 'Body goes here', 'from@example.com',
                    ['to1@example.com', 'to2@example.com'], ['bcc@example.com'],
                    reply_to=['another@example.com'], headers={'Message-ID': 'foo'})"""


