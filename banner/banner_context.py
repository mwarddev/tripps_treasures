from .models import Banner


def info_banner(request):
    """ Output banner info """
    banners = Banner.objects.all()
    context = {
        'banners': banners,
    }

    return context
