# In your_app/views.py

from django.views.generic import ListView
from .models import Songs as Song   
from django.shortcuts import render, get_object_or_404



# Lists all songs (The main screen)
class SongListView(ListView):
    model = Song
    template_name = 'songs.html'  # Template for the main list
    context_object_name = 'songs'

# In your_app/views.py (continued)


def song_detail(request, id):
    song = get_object_or_404(Song, pk=id)
    return render(request, 'songLyric.html', {'song': song})