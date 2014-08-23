from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# ... the rest of your URLconf goes here ...


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangotodo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^add/', include(admin.site.urls)),
    url(r'^new/', include(admin.site.urls)),
    url(r'^$', 'todo.views.index'),
)
urlpatterns += staticfiles_urlpatterns()
