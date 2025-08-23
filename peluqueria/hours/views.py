from django.shortcuts import render
from .models import Hours, Info
from django.views.generic import TemplateView

# Create your views here.


class HoursView(TemplateView):
    template_name = 'hours/open.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = Info.objects.first()
        context['hours'] = Hours.objects.all()

        return context
