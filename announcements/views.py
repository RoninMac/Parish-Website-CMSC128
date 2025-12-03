from django.views.generic import ListView
from .models import Announcement  
from django.shortcuts import render, get_object_or_404
# Create your views here.

class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcements.html'  # Template for the main list
    context_object_name = 'announcements'

def announcement_detail(request, id):
    announcement = get_object_or_404(Announcement, pk=id)
    return render(request, 'announcementDetailS.html', {'announcement': announcement})