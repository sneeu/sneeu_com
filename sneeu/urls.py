from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin


urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^', include('apps.blog.urls')),
    (r'^', include('apps.core.urls')),
)


if settings.DEBUG == True:
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
    )
