from django.urls import path
from . import views

urlpatterns = [
    path('', views.PriestListView.as_view(), name='priest_list'),
    path('priest/<int:id>/', views.priest_detail, name='priest_detail'),
]