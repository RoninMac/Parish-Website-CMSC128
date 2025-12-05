# In your views.py file
from django.shortcuts import render, redirect
from .models import DonationInfo # Assuming you have a Donation model
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404

from .forms import DonationForm
def donate_view(request):
    if request.method == 'POST':
        # --- 1. MANUALLY RETRIEVE ALL FIELDS ---
        name = request.POST.get('donor-name')
        email = request.POST.get('donor-email')
        amount = request.POST.get('donation-amount')
        message = request.POST.get('donor-message', '')  # Optional field
        
        is_anonymous = request.POST.get('anonymous-checkbox')
        
        if is_anonymous == 'on':
            # If the checkbox was checked, override the name field.
            name = "Anonymous"
        # --- 2. PERFORM MANUAL VALIDATION (REQUIRED since you skip Django Forms) ---
        if name and email and amount:
            try:
                # Convert amount to a number/decimal before saving
                amount = float(amount) 
                
                # --- 3. SAVE to the database ---
                DonationInfo.objects.create(
                    name=name,
                    email=email,
                    amount=amount,
                    message=message
                )
                
                # --- 4. REDIRECT ---
                return redirect('thank_you') 

            except ValueError:
                # Handle non-numeric amount error here
                pass 
            
        # If any validation fails, re-render the template with an error message
       
    else: 
        form = DonationForm()    
    return render(request, 'donate.html', {'form': form})

def thank_you(request):
    return render(request, 'thankyou.html')

class DonationListView(ListView):
    model = DonationInfo
    template_name = 'donationAknowledgementPage.html'  # Template for the main list
    context_object_name = 'donations'