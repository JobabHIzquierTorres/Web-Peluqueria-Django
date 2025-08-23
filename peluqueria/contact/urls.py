from .views import ContactView
from django.urls import path

contact_patterns = ([
    path('', ContactView.as_view(), name='contact')
]), 'contact'
