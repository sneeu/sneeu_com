from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext, TemplateDoesNotExist


def template_from_path(request, path):
    if path == '':
        path = 'index'
    if path[-1] == '/':
        path = path[:-1]

    try:
        return render_to_response('pages/%s.html' % path, {},
            RequestContext(request))
    except TemplateDoesNotExist:
        raise Http404, u"Template does not exist."
