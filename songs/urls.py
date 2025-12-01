# In your_app/urls.py

from django.urls import path
from .views import SongListView
from . import views

urlpatterns = [
    # Main list view (The screen from your image)
    path('', SongListView.as_view(), name='song-list'),
    path('song/<int:id>/', views.song_detail, name='song_detail'),
]