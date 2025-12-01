from django.shortcuts import render, redirect
from .forms import AdminPersonCreationForm
# Create your views here.
def admin_login(request):
    return render(request, 'login.html')

def admin_success(request):
    return render(request, 'loginSuccess.html')

def admin_register(request):
    if request.method == 'POST':
        form = AdminPersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_success')
    else:
        form = AdminPersonCreationForm()
    return render(request, 'register.html', {'form': form})
