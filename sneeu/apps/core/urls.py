from django.conf.urls.defaults import *

import views


urlpatterns = patterns('',
    url(r'^404/$', views.four_oh_four),
    url(r'^500/$', views.five_hundred),
)