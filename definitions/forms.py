from django import forms
from .models import Definition

class DefinitionForm(forms.ModelForm):
    class Meta:
        model = Definition
        fields = ['definition']




