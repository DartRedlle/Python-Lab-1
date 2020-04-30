from django import forms

from .models import Massage

class MassageForm(forms.ModelForm):

    class Meta:
        model = Massage
        fields = ('header', 'text',)