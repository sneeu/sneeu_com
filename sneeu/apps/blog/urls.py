from django.conf.urls.defaults import *

import feeds
import views


urlpatterns = patterns('',
    url(r'^$', views.post_list),
    url(r'^blog/(?P<year>\d{4})/(?P<month>\d{2})/(?P<slug>[^/]+)/$',
        views.post_detail, name='post_detail'),
    url(r'^blog/(?P<url>[a-z]+)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': feeds.FEEDS}),
)