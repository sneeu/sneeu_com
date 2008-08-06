from django.conf.urls.defaults import *

import views


urlpatterns = patterns('',
    url(r'^(?P<path>.*)/$', views.template_from_path),
)