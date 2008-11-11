from django.conf.urls.defaults import *

from models import Log
import views


info_dict = {
    'queryset': Log.objects.all().select_related(),
    'paginate_by': 20,
}


urlpatterns = patterns('',
    url(r'^$',
        'django.views.generic.list_detail.object_list', info_dict, name='log_list'),
    url(r'^tumble/update/$',
        views.update, name='update'),
    # url(r'^tumble/(?P<year>\d{4})/(?P<month>1[012]?|[2-9])/(?P<slug>[^/]+)/$',
    #     views.post_detail, name='post_detail'),
    # url(r'^tumble/(?P<year>\d{4})/(?P<month>1[012]?|[2-9])/(?P<slug>[^/]+)/add-comment/$',
    #     views.add_comment, name='add_comment'),
    # url(r'^tumble/(?P<url>[a-z]+)/$', 'django.contrib.syndication.views.feed',
    #     {'feed_dict': feeds.FEEDS}),
)