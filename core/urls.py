from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('history/', views.history, name='history'),
    path('location/', views.location, name='location'),
    path('admin-redirect/', views.go_to_admin, name='go_to_admin'),
]