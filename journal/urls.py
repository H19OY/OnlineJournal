from django.urls import path
from . import views

urlpatterns = [
    path('entry/create/', views.create_entry, name='create_entry'),
    path('entry/list/', views.entry_list, name='entry_list'),
]
