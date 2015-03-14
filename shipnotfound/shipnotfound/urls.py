from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from registration.backends.simple.views import RegistrationView


class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/home'



urlpatterns = patterns('',


    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', '_404shipnotfound.views.index', name='index'),
    url(r'^home/', '_404shipnotfound.views.home', name='home'),
    (r'^accounts/', include('registration.backends.simple.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )