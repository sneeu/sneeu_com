from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext


def four_oh_four(request):
    raise Http404


def five_hundred(request):
    raise RuntimeError
