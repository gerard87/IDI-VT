from django.conf.urls import url, patterns, include
from django.core.urlresolvers import reverse_lazy
from views import idivt_view, idivt_send, rotate_galaxy, exit_rotate_galaxy, import_data
from django.views.generic.base import RedirectView


urlpatterns = [

    url(r'^$',
        RedirectView.as_view(url=reverse_lazy('idivt:idivtview')),
        name='home_page'),

    url(r'^idivt.html$',
        idivt_view.as_view(),
        name='idivtview'),

    url(r'^idivt/send/(?P<key>\w+)/$',
        idivt_send,
        name='idivtsend'),

    url(r'^idivt/rotate/(?P<key>\w+)/$',
        rotate_galaxy,
        name='idivtrotate'),

    url(r'^idivt/exitrotate/(?P<key>\w+)/$',
        exit_rotate_galaxy,
        name='idivtexitrotate'),

    url(r'^idivt/import/$',
        import_data,
        name='idivtimport'),

]
