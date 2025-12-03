from django.views.generic import ListView
from .models import Groups
from django.shortcuts import render, get_object_or_404
# Create your views here.

class GroupsListView(ListView):
    model = Groups
    template_name = 'groups.html'  # Template for the main list
    context_object_name = 'groups'

def group_detail(request, id):
    group = get_object_or_404(Groups, pk=id)
    return render(request, 'groupDetails.html', {'group': group})
