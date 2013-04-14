from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),

    url(r"^notifications/", include("notifications.urls")),
    url(r"^account/", include("account.urls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^torrents/', include("torrents.urls")),
    url(r'^music/', include("music.urls"))
)
