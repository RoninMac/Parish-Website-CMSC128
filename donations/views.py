"""
========================================
DONATIONS VIEWS - Handling Monetary Contributions
========================================
Processes donation submissions from the public.

FEATURES:
  - Handles donation form submission (POST)
  - Validates donor information via DonationForm (ModelForm)
  - Saves valid donations to Donation model
  - Displays thank you page after successful submission
  - Allows optional donor message/prayer request

DATABASE INTERACTION:
  - Donation model: Stores name, email, amount, message, date
  - Model defined in donations/models.py

IMPROVEMENTS NEEDED:
  - Add email notification/receipt to donor
  - Add donor receipt generation/download
  - Implement payment gateway for online transactions
  - Add form field validation (e.g., minimum donation amount)
  - Add success message to context (currently just redirect)
  - Add logging for donation tracking and debugging
  - Add error handling for form.save() failures
  - Add donation receipts/certificates

FUTURE ENHANCEMENTS:
  - Payment processing (Stripe, PayMongo)
  - Email receipts and thank you letters
  - Anonymous donation option
  - Recurring donations
  - Donor management/relationship tracking
========================================
"""

from django.shortcuts import render, redirect
from .forms import DonationForm


def donate(request):
    """
    Handle donation form submission and display.
    
    
    GET REQUEST:
      - Display empty donation form
      - User can enter: name, email, amount, optional message
      
    POST REQUEST:
      - Validate submitted form data
      - If valid: Save donation to database, show thank you page
      - If invalid: Re-display form with error messages for user correction
    
    
    FORM FIELDS (from DonationForm):
      - name (CharField, max_length=100): Donor's full name (required)
      - email (EmailField): Donor's email (required, must be valid)
      - amount (DecimalField): Donation amount in Philippine Pesos ₱ (required, max 999,999.99)
      - message (TextField): Optional prayer request or message (optional, blank=True)
    """

    if request.method == 'POST':
        # Handle form submission from POST request
        form = DonationForm(request.POST)
        
        if form.is_valid():
            # Form validation passed
            # All required fields present and valid format (e.g., valid email)
            # Save the donation record to database
            form.save()
            
            # Redirect to thank you page
            # TODO: Consider passing donation_id or message context
            return render(request, 'thankyou.html')
        # If form invalid, fall through to re-render donate.html with error messages
    
    else:
        # GET request: Display empty form
        form = DonationForm()
    
    # Render donation form template with form instance
    # Form displays fields: name, email, amount, message
    # If POST with errors, form displays error messages for invalid fields
    return render(request, 'donate.html', {'form': form})
