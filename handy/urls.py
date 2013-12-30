from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# admin.autodiscover()
from markme import  views
import markme

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'handy.views.home', name='home'),
    # url(r'^handy/', include('handy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^latest/$', views.latest_gays),
    url(r'^add/$', views.show_add_page),
    url(r'^$',markme.views.indexPage),
    url(r'^test/$',markme.views.indexPage),
    url(r'^post_add_gays/$',markme.views.post_add_gays)
)

