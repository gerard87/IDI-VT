from django.shortcuts import render
from models import Line
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class idivt_view(ListView):
    model = Line
    template_name = 'idivt/idivt.html'
    context_object_name = 'lines_list'

def idivt_send(request, key):

    line = Line.objects.get(pk=key)

    if line.visibility:
        line.visibility = False
    else:
        line.visibility = True
    line.save()

    #folderKML = BASE_DIR+'/static/idivt/'+line.name
    #flyto(system.name)
    #write_kml(folderKML, "idivt", line.name, line.visibility)

    return HttpResponseRedirect(reverse('idivt:idivtview'),{})
