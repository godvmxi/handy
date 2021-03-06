from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from markme import  views
import markme
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'handy.views.home', name='home'),
    # url(r'^handy/', include('handy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^list/$', views.list_gays),
    url(r'^add/$', views.add_gay),
    url(r'^$',markme.views.indexPage),
    url(r'^edit/(\d{1,10})/$',markme.views.edit_gay),
    url(r'^detail/(\d{1,10})/$',markme.views.detail_gay),
    url(r'^list/(\d{1,10})/delete/$',markme.views.delete_gay),
    url(r'^cookie/$',markme.views.request_cookie),
    # url(r'^resource/(?P<path>.*)','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)
if settings.DEBUG:
    urlpatterns+= patterns('',
    url(r'^resource/(?P<path>.*)','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)
