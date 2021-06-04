from django import forms
from django.db.models import fields
from django.forms.models import model_to_dict
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"