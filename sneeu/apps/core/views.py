from django.http import Http404


def four_oh_four(request):
    raise Http404


def five_hundred(request):
    raise RuntimeError
