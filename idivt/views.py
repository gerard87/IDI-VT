from django.shortcuts import render
from models import Line
from django.views.generic import ListView


class idivt_view(ListView):
    model = Line
    template_name = 'idivt/idivt.html'
    context_object_name = 'lines_list'
