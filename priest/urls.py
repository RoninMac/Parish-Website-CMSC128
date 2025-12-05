from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PriestListView.as_view(), name='priest_list'),
    path('priest/<int:id>/', views.priest_detail, name='priest_detail'),
]

