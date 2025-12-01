# forms.py
from django import forms
from .models import AdminPerson

class AdminPersonCreationForm(forms.ModelForm):
    class Meta:
        model = AdminPerson
        fields = ['email', 'password']
    password = forms.CharField(widget=forms.PasswordInput)



