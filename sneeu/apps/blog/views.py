from django.core.cache import cache
from django.core.paginator import QuerySetPaginator
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_page

from apps.session_messages.helpers import add_message

from forms import AddPostCommentForm
from models import Post, PostComment


def post_list(request):
    page_no = request.GET.get('page', 1)

    if page_no == 1:
        cached_page = cache.get('/')
        if cached_page:
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
            'comment_form': AddPostCommentForm(),
            'object': post,
        }
        response = render_to_response('blog/post_detail.html', context,
            RequestContext(request))

        cache.set(request.path, response)
    return response


def add_comment(request, year, month, slug):
    MESSAGES = {
        'comments_closed': u"Sorry, comments are closed for this post.",
    }

    post = get_object_or_404(Post, created__year=int(year),
        created__month=int(month), slug=slug)
    if request.method == 'POST':
        message = None
        if not post.comments_open:
            add_message(request, MESSAGES['comments_closed'])
            return HttpResponseRedirect(comment.get_absolute_url())
        else:
            form = AddPostCommentForm(request.POST)
            if form.is_valid():
                comment = PostComment.objects.create(
                    post=post,
                    author_name=form.cleaned_data['author_name'],
                    author_url=form.cleaned_data['author_url'],
                    copy=form.cleaned_data['copy'],
                )
                return HttpResponseRedirect(comment.get_absolute_url())
        context = {'form': form, 'object': post}
        return render_to_response('blog/add_comment.html', context,
            RequestContext(request))
    else:
        return HttpResponseNotAllowed(['POST'])
