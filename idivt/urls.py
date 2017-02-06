from django.conf.urls import url, patterns, include
from django.core.urlresolvers import reverse_lazy
from views import idivt_view, idivt_send
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

]
