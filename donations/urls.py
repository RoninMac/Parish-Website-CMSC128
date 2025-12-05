from django.urls import path
from . import views

urlpatterns = [
    # When this urls module is included at 'donate/' in the project urls,
    # this '' pattern will produce the final URL '/donate/'.
    path('', views.donate_view, name='donate'),
    path('thankyou/', views.thank_you, name='thank_you'),
    path('acknowledgements/', views.DonationListView.as_view(), name='donation_acknowledgements'),
]
