from django.urls import path

import donations
from . import views
from donations.views import DonationListView

urlpatterns = [
    path('', views.index, name='home'),
    path('history/', views.history, name='history'),
    path('location/', views.location, name='location'),
    path('admin-redirect/', views.go_to_admin, name='go_to_admin'),
    path('acknowledgements/', donations.views.DonationListView.as_view(), name='donation_acknowledgements'),
]