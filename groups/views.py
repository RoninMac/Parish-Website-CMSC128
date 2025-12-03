from django.views.generic import ListView
from .models import ChurchGroups
from django.shortcuts import render, get_object_or_404
# Create your views here.

class GroupsListView(ListView):
    model = ChurchGroups
    template_name = 'group.html'  # Template for the main list
    context_object_name = 'groups'

def group_detail(request, id):
    group = get_object_or_404(ChurchGroups, pk=id)
    return render(request, 'groupDetails.html', {'group': group})
