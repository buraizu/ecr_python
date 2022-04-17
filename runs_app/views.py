from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse

pages = {
    'runs': 'List Runs',
    'add_run': 'Add Run',
    'run_stats': 'Running Statistics'
}

# Create your views here.
def runs_view(request, topic):
    try:
        result = pages[topic]
        return HttpResponse(pages[topic])
    except:
        raise Http404("404 Generic Error") # Can connect to 404 template
