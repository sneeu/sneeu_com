from django.core.cache import cache
from django.core.paginator import QuerySetPaginator
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_page

from models import Post


def post_list(request):
    page_no = request.GET.get('page', 1)

    if page_no == 1:
        cached_page = cache.get('/')
        if cached_page:
            cached_page['X-Cache'] = 'Hit'
            return cached_page

    paginator = QuerySetPaginator(Post.objects.all(), 10)
    context = {
        'paginator': paginator,
        'page': paginator.page(page_no),
    }
    response = render_to_response('blog/post_list.html', context,
        RequestContext(request))

    if page_no == 1:
        cache.set('/', response)

    return response


def post_detail(request, year, month, slug):
    response = cache.get(request.path)
    if not response:
        post = get_object_or_404(Post, created__year=int(year),
            created__month=int(month), slug=slug)
        context = {
            'object': post,
        }
        response = render_to_response('blog/post_detail.html', context,
            RequestContext(request))

        cache.set(request.path, response)
    else:
        response['X-Cache'] = 'Hit'
    return response