from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^nithin',hello.views.nithin, name = 'nithin'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$',hello.views.logout_page),
    url(r'^register/$', hello.views.register_page),
    url(r'^schedule_pickup/$', hello.views.schedule_pickup),
]
