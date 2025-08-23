from django.urls import path
from .views import AboutView


about_patterns = ([
    path('', AboutView.as_view(), name='about')

]), 'about'
