from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('cdr.views',
    # Examples:
    # url(r'^$', 'ilabs_site.views.home', name='home'),
    # url(r'^ilabs_site/', include('ilabs_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'test'),
    url(r'^call_details/', 'call_details'),
    url(r'^get_data/', 'get_data'),
    url(r'^get_pie_data/', 'get_pie_data'),
    url(r'^process_data/', 'process_data'),
    url(r'^process_pie_data/', 'process_pie_data'),
    url(r'^addtag/(?P<cntid>\d+)', 'addtag'),
)
