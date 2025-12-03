from django.urls import path 
from . import views

urlpatterns = [
    path('', views.GroupsListView.as_view(), name='group_list'), 
    path('group/<int:id>/', views.group_detail, name='group_detail'),
]