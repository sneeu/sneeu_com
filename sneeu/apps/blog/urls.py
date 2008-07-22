from django.conf.urls.defaults import *

import feeds
import views


urlpatterns = patterns('',
    url(r'^$', views.post_list),
    url(r'^blog/(?P<year>\d{4})/(?P<month>1[012]?|[2-9])/(?P<slug>[^/]+)/$',
        views.post_detail, name='post_detail'),
    url(r'^blog/(?P<year>\d{4})/(?P<month>1[012]?|[2-9])/(?P<slug>[^/]+)/add-comment/$',
        views.add_comment, name='add_comment'),
    url(r'^blog/(?P<url>[a-z]+)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': feeds.FEEDS}),
)