from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Prices, Info

# Create your views here.


class PricesView(TemplateView):
    template_name = 'prices/price.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['prices'] = Prices.objects.all()
        context['info'] = Info.objects.first()

        return context
