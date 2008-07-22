from django.shortcuts import render_to_response
from django.template import RequestContext


def template_from_path(request, path):
    if path == '':
        path = 'index'
    if path[-1] == '/':
        path = path[:-1]

    return render_to_response('projects/%s.html' % path, {},
        RequestContext(request))
