from django.views.generic import ListView
from .models import Priest
from django.shortcuts import render, get_object_or_404
# Create your views here.

class PriestListView(ListView):
    model = Priest
    template_name = 'priest.html'  # Template for the main list
    context_object_name = 'priests' 

def priest_detail(request, id):
    priest = get_object_or_404(Priest, pk=id)
    return render(request, 'priestDetails.html', {'priest': priest})