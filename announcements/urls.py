from django.urls import path
from . import views

urlpatterns = [
    path('', views.AnnouncementListView.as_view(), name='announcement_list'),
    path('announcement/<int:id>/', views.announcement_detail, name='announcement_detail'),
]