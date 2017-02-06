from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from liquidgalaxy.lgCommunication import write_kml, flyto
from liquidgalaxy.kml_generator import create_line_kml
from IDIVT.settings import BASE_DIR
from models import Line, Tower


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

        ls = Line.objects.all()
        for l in ls:
            if l != line:
                l.visibility = False
                l.save()

        flyto(line.name)
    line.save()

    folderKML = BASE_DIR+'/static/kml/'

    towers = Tower.objects.filter(line=line)
    create_line_kml(line, towers)

    write_kml(folderKML, "idivt", line.name, line.visibility)

    return HttpResponseRedirect(reverse('idivt:idivtview'),{})
