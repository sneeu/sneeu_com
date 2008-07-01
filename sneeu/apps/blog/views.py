from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from models import Post


def post_list(request, page=1):
    posts = Post.objects.all()

    context = {
        'object_list': posts,
    }

    return render_to_response('blog/post_list.html', context,
        RequestContext(request))


def post_detail(request, year, month, slug):
    post = get_object_or_404(Post, created__year=int(year),
        created__month=int(month), slug=slug)

    context = {
        'object': post,
    }

    return render_to_response('blog/post_detail.html', context,
        RequestContext(request))
