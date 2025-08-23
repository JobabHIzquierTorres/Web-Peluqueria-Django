from .models import Services

"""
  Variable Global accesible en todos los templates, se usa en about/includes/base_about.html
  Hay que activarlo en:    Settings
"""


def services_ctx(request):
    try:
        services = Services.objects.all().order_by('title')
    except Services.DoesNotExist:
        services = None
        print('Sin contenido en servicios')
    return {'services': services}
