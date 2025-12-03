from django import forms
from .models import groups

class GroupsForm(forms.ModelForm):
    class Meta:
        model = groups
        fields = ['name', 'description', 'created_at']