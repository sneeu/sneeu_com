from django.conf import settings
from django.contrib.sites.models import Site


def media_url(request):
    return {'media_url': settings.MEDIA_URL}


def current_site(request):
    return {'site': Site.objects.get_current()}