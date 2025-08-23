from .models import Info, Prices


def info_ctx(request):
    try:
        info = Info.objects.first()
    except Info.DoesNotExist:
        info = None
        print('No hay Info-prices')

    return {'info_prices': info}


def prices_ctx(request):
    try:
        prices = Prices.objects.all()
    except Prices.DoesNotExist:
        prices = None
        print('No hay Prices-prices')

    return {'prices_prices': prices}
