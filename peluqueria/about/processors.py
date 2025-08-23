from .models import About

"""
  Variable Global accesible en todos los templates, se usa en about/includes/base_about.html
  Hay que activarlo en:    Settings

"""


def about_ctx(request):

    try:
        about = About.objects.latest('created')
    except About.DoesNotExist:
        about = None

    return {'about_info': about}
