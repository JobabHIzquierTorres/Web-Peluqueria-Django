from django import template

"""
  Obtener el nombre de la ruta, creando un tag para el template escogido (core/template/includes/header.html)
"""

register = template.Library()


@register.simple_tag(takes_context=True)
def pg_actual(context):
    path = context['request'].path

    mapping = {
        '/about/': 'Nosotros',
        '/services/': 'Servicios',
        '/prices/': 'Precios',
        '/hours/': 'Horario',
        '/contact/': 'Contacto'
    }

    return mapping.get(path, 'Página')
