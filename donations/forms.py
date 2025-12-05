"""
========================================
DONATIONS FORMS - User Input Handling
========================================
Forms for processing donation submissions.

FORMS:
  - DonationForm: Handles donor information and donation amount

DATABASE VALIDATION:
  - Email: Must be unique per donation [to be implemented]
  - Amount: Must be positive decimal, max ₱999,999.99
  - Name: Max 100 characters
  - Message: Optional, plain text

FUTURE ENHANCEMENTS:
  - Add donor anonymity checkbox
  - Add payment method selection before processing
========================================
"""
from django import forms
from .models import DonationInfo

class DonationForm(forms.ModelForm):
    class Meta:
        model = DonationInfo
        fields = ['name', 'email', 'amount', 'message']
