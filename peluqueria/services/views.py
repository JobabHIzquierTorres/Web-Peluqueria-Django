from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Services

# Create your views here.


class ServicesView(TemplateView):
    template_name = 'services/service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Services.objects.all()
        return context
