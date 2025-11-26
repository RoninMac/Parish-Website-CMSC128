"""
========================================
DONATIONS VIEWS - Handling Monetary Contributions
========================================
Processes donation submissions from the public.

APP ROUTES:
  - '/donate/' -> donate view (GET/POST)

FEATURES:
  - Handles donation form submission (POST)
  - Validates donor information via DonationForm (ModelForm)
  - Saves valid donations to Donation model
  - Displays thank you page after successful submission
  - Allows optional donor message/prayer request

REQUEST FLOW:
  1. GET /donate/ -> Display empty donation form
  2. POST /donate/ -> Validate form data
     - Valid -> Save to database, show thank you page
     - Invalid -> Re-display form with error messages

TEMPLATES USED:
  - donate.html: Form display (GET request)
  - thankyou.html: Success confirmation (POST after valid submission)

DATABASE INTERACTION:
  - Donation model: Stores name, email, amount, message, date
  - Model defined in donations/models.py

IMPORTANT NOTES:
  - NO email notification sent to donor (TODO: Add confirmation email)
  - NO payment gateway integration (TODO: Integrate PayMongo/Stripe)
  - Form fields: name, email, amount, message (optional)
  - All donations stored in Philippine Pesos (₱)
  - NO donor receipt generation yet

SECURITY NOTES:
  ✓ CSRF protection: Provided by Django middleware (ensure {% csrf_token %} in template)
  ✓ Email validation: Handled by DonationForm's EmailField
  ✓ SQL injection prevention: Django ORM automatically sanitizes queries
  ✓ XSS prevention: Template rendering escapes HTML by default
  
  TODO: Add server-side amount validation (min/max limits)
  TODO: Add spam detection (honeypot field, rate limiting)
  TODO: Add IP blocking for repeated failed submissions

IMPROVEMENTS NEEDED:
  - Add email notification/receipt to donor
  - Add donor receipt generation/download
  - Implement payment gateway for online transactions
  - Add form field validation (e.g., minimum donation amount)
  - Add success message to context (currently just redirect)
  - Add logging for donation tracking and debugging
  - Add error handling for form.save() failures
  - Add donation receipts/certificates

ADMIN ACCESS:
  - View all donations: Django admin panel
  - Filter by date, amount, donor name
  - See admin configuration in donations/admin.py

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
    
    ROUTE: /donate/ (GET and POST)
    
    GET REQUEST:
      - Display empty donation form
      - User can enter: name, email, amount, optional message
      
    POST REQUEST:
      - Validate submitted form data
      - If valid: Save donation to database, show thank you page
      - If invalid: Re-display form with error messages for user correction
    
    PARAMETERS:
      - request (HttpRequest): The HTTP request object
    
    RETURNS:
      - GET: render(request, 'donate.html', {'form': DonationForm()})
      - POST (valid): render(request, 'thankyou.html')
      - POST (invalid): render(request, 'donate.html', {'form': form_with_errors})
    
    CONTEXT DATA PASSED TO TEMPLATES:
      - donate.html: {'form': DonationForm instance}
      - thankyou.html: No context (static thank you page)
    
    FORM FIELDS (from DonationForm):
      - name (CharField, max_length=100): Donor's full name (required)
      - email (EmailField): Donor's email (required, must be valid)
      - amount (DecimalField): Donation amount in Philippine Pesos ₱ (required, max 999,999.99)
      - message (TextField): Optional prayer request or message (optional, blank=True)
    
    DATABASE CHANGES:
      - New Donation record created in donations_donation table
      - Fields: id (auto), name, email, amount, message, date (auto timestamp)
    
    WORKFLOW EXAMPLE:
      1. User navigates to /donate/ (GET)
         -> See empty form with fields: name, email, amount, message
      
      2. User fills form:
         name: "Maria Santos"
         email: "maria@example.com"
         amount: 500.00
         message: "For the chapel restoration"
      
      3. User clicks submit (POST)
         -> Form validates email format and amount
      
      4. If valid:
         -> Donation record saved to database
         -> Redirect to /donate/thankyou/ page
         -> User sees thank you message
      
      5. If invalid (e.g., bad email):
         -> Form re-displays with error messages
         -> User sees which field has error
    
    ERROR HANDLING:
      - Invalid email format: Form validation catches and displays error
      - Missing required field: Form validation catches and displays error
      - Database save error: Currently NOT handled (TODO: Add try/except)
      
    NOTES:
      - Form instance created fresh for GET requests
      - Form bound with POST data for POST requests
      - form.is_valid() runs all field validators and model validators
      - form.save() creates new Donation record with auto timestamp
    
    TODO:
      - Add email confirmation sent to donor
      - Add donation receipt download/PDF generation
      - Add success message with donation details
      - Add error handling for database failures
      - Add logging for monitoring donations
      - Add spam detection/prevention
      - Add rate limiting (prevent same user submitting repeatedly)
    
    RELATED MODELS/FORMS/TEMPLATES:
      - Model: donations.models.Donation
      - Form: donations.forms.DonationForm
      - Template (GET): donations/templates/donate.html
      - Template (POST success): donations/templates/thankyou.html
      - Admin: donations/admin.py (register Donation model)
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
