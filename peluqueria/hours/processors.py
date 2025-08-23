from .models import Hours, Info


def hours_ctx(request):
    try:
        hours = Hours.objects.all()
    except Hours.DoesNotExist:
        hours = None
        print('No hay horario en hours')

    return {'hours_hours': hours}


def info_ctx(request):
    try:
        info = Info.objects.first()
    except Info.DoesNotExist:
        info = None
        print("No hay info en hours")

    return {'info_hour': info}
