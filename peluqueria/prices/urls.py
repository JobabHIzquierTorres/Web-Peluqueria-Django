from django.urls import path
from .views import PricesView

prices_patterns = [(
    path('', PricesView.as_view(), name='prices')
)], 'prices'
