from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#handler404 = 'site_config.views.pagenotfound'

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'ilabs_site.views.home', name='home'),
    url(r'^$', 'views.home', name='home'),
    # url(r'^ilabs_site/', include('ilabs_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/', 'django.contrib.auth.views.login'),
    url(r'^cdr/', include('cdr.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
