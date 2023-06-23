from django.urls import path 
from . import views

urlpatterns = [
    path('drivers/', views.DriverListAPIView.as_view(), name='driver-list'),
    path('missions/', views.MissionListAPIView.as_view(), name='mission-list'),
]