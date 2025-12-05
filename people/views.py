
from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from .models import Subscription
from .forms import SubscriptionForm
		
def subscribe(request):
	if request.method == 'POST':

		email = request.POST.get('email')
		password = request.POST.get('password')


		if email and password:
			try:
				Subscription.objects.create(
					email=email,
					password=password
				)
				return redirect('thank_you')
			
			except IntegrityError:
            # Handle the case where the email already exists
            # You would typically add a message to the user here
				return render(request, 'subscribe_page.html', {
					'error_message': 'This email address is already subscribed.'
				})
        
			except Exception as e:
				# Catch other unexpected database or system errors
				print(f"An unexpected error occurred: {e}")
				return render(request, 'subsscribe.html')
			

def thank_you(request):
	return render(request, 'thankyouSub.html')

def subscriptionPage(request):
	return render(request, 'subscribe.html')