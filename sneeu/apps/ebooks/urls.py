from django.conf.urls.defaults import *

import views


urlpatterns = patterns('',
    url(r'^$', views.book_list),
    url(r'^(?P<book_slug>[^/]+)/$', views.book_detail, name='book_detail'),
    url(r'^(?P<book_slug>[^/]+)/(?P<chapter>\d+)/$', views.chapter_detail,
        name='chapter_detail'),
)