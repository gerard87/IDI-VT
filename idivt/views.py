from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import time

from liquidgalaxy.lgCommunication import write_kml, flyto, send_single_kml, start_tour, exit_tour
from liquidgalaxy.kml_generator import create_line_kml2, create_tour_rotation_kml, create_line_kmz
from IDIVT.settings import BASE_DIR
from models import Line, Tower


class idivt_view(ListView):
    model = Line
    template_name = 'idivt/idivt.html'
    context_object_name = 'lines_list'

def idivt_send(request, key):

    line = Line.objects.get(pk=key)

    folderKML = BASE_DIR+'/static/kml/'
    folderImg = BASE_DIR+'/static/img/'
    millis = int(round(time.time()*1000))

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
        towers = Tower.objects.filter(line=line)
        create_line_kml2(line, towers)
        create_line_kmz(line, folderKML, folderImg, millis)

    line.save()

    write_kml(folderKML, "idivt", line.name, line.visibility, millis)

    return HttpResponseRedirect(reverse('idivt:idivtview'),{})




def rotate_galaxy(request, key):
    line = Line.objects.get(pk=key)
    kml = create_tour_rotation_kml(line)
    send_single_kml(kml)
    start_tour()
    return HttpResponseRedirect(reverse('idivt:idivtview'),{})

def exit_rotate_galaxy(request, key):
    exit_tour()
    return HttpResponseRedirect(reverse('idivt:idivtview'),{})
