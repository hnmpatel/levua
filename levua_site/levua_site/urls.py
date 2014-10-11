from django.conf.urls import patterns, include, url
from people import urls as people_urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'levua_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home', 'levua_site.views.home'),
    url(r'^about', 'levua_site.views.about'),
    url(r'^blog', 'levua_site.views.blog'),
    url(r'^contact', 'levua_site.views.contact'),
    url(r'^people/', include(people_urls)),
)
