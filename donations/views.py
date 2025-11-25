from django.shortcuts import render, redirect
from .forms import DonationForm

def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thankyou.html')
    else:
        form = DonationForm()
    return render(request, 'donate.html', {'form': form})
