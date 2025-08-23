from django.urls import path
from .views import ServicesView

services_patterns = ([
    path('', ServicesView.as_view(), name='services')
]), 'services'
