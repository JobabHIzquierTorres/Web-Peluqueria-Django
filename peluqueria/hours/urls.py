from django.urls import path
from .views import HoursView

hours_patterns = ([
    path('', HoursView.as_view(), name='hours')
]), 'hours'
