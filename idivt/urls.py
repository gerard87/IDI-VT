from django.conf.urls import url, patterns, include
from django.core.urlresolvers import reverse_lazy
from views import idivt_view
from django.views.generic.base import RedirectView

urlpatterns = patterns('',

    url(r'^$',
        RedirectView.as_view(url=reverse_lazy('idivt:idivt')),
        name='home_page'),

    url(r'^idivt.html$',
        idivt_view.as_view(),
        name='idivt'),



)
