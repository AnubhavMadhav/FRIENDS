# map_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add_location/', views.add_location, name='add_location'),
    path('map/', views.map_view, name='map_view'),
]