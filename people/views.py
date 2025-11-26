"""
========================================
PEOPLE VIEWS - Subscription Management
========================================
Views for managing email subscriptions.

ROUTE:
  - 'subscribe/' -> subscribe() (GET/POST)

TEMPLATES: subscribe.html, thankyouSub.html
========================================
"""

from django.shortcuts import render, redirect
from .models import Subscription
from django import forms

class SubscriptionForm(forms.ModelForm):
	class Meta:
		model = Subscription
		fields = ['email']
		
def subscribe(request):
	"""
	Handle email subscription page (GET and POST).
	
	GET: Display empty subscription form
	POST: Process form submission
	  - If valid: Save subscription, show thank you page
	  - If invalid: Show form with errors (e.g., duplicate email)
	
	FORM DATA:
	  - email: User's email address
	
	TODO: 
	  - Add IntegrityError handling for duplicate emails (show friendly message)
	  - Add email confirmation/double opt-in
	  - Add success message using Django messages framework
	"""
	if request.method == 'POST':
		form = SubscriptionForm(request.POST)
		if form.is_valid():
			# Save the subscription to database
			form.save()
			# Show thank you page after successful subscription
			return render(request, 'thankyouSub.html')
	else:
		# GET request: show empty form
		form = SubscriptionForm()
	
	# Render form page with context
	return render(request, 'subscribe.html', {'form': form})