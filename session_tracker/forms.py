from django import forms

from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_name', 'sessions']
        labels = ['Client:']