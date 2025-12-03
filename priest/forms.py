from django import forms
from .models import Priest  

class PriestForm(forms.ModelForm):
    class Meta:
        model = Priest
        fields = ['name', 'birthdate', 'bio', 'photo']