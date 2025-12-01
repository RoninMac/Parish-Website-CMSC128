from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.admin_login, name='admin_login'),
    path('loginSucessful/', views.admin_success, name='admin_success'),
]