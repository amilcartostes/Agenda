from django.db import models
from django import forms
from contatos.models import Contact


# Criando formulário
class FormContact(forms.ModelForm):
    class Meta:
        model = Contact
        # exclude = ('show',)
        exclude = ()



