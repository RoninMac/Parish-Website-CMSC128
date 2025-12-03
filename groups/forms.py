from django import forms
from .models import ChurchGroups

class GroupsForm(forms.ModelForm):
    class Meta:
        model = ChurchGroups
        fields = ['name', 'description', 'created_at', 'posted_by']