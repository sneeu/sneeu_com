from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from models import Book, Chapter


def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render_to_response('ebooks/book_list.html', context,
        RequestContext(request))


def book_detail(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    context = {
        'book': book,
    }
    return render_to_response('ebooks/book_detail.html', context,
        RequestContext(request))


def chapter_detail(request, book_slug, chapter):
    chapters = Chapter.objects.filter(book__slug=book_slug)
    paginator = Paginator(chapters, 1)
    chapter = paginator.page(chapter).object_list[0]
    context = {
        'chapter': chapter,
        'paginator': paginator,
    }
    return render_to_response('ebooks/chapter_detail.html', context,
        RequestContext(request))
