from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from liquidgalaxy.lgCommunication import write_kml, flyto, send_single_kml, start_tour, exit_tour
from liquidgalaxy.kml_generator import create_line_kml, create_tour_rotation_kml, create_line_kmz
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
    filename = ""

    if line.visibility:
        line.visibility = False
    else:
        line.visibility = True

        ls = Line.objects.all()
        for l in ls:
            if l != line:
                l.visibility = False
                l.save()


        towers = Tower.objects.filter(line=line)
        dst = str(towers[0].latitude)+","+str(towers[0].longitude) if len(towers) > 0 else line.name
        flyto(dst)
        create_line_kml(line, towers)
        filename = create_line_kmz(line, folderKML, folderImg)

    line.save()

    write_kml(folderKML, "idivt", filename, line.visibility)

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
