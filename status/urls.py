from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('status.views',
    # Examples:
    # url(r'^$', 'status.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'index'),
    url(r'^incidents/(?P<pk>\d+)$', 'incident', name='incident'),
    url(r'^history$', 'history', name='history'),
)
