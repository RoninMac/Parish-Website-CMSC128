from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscriptionPage, name='subscribe_page'),
    path('thankyou/', views.thank_you, name='thank_you'),
    path('submit/', views.subscribe, name='subscribe'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
]
