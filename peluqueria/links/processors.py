from .models import Links


def links_ctx(request):

    ctx = {}

    links = Links.objects.all()

    for link in links:
        ctx[link.key] = link.url

    return ctx
