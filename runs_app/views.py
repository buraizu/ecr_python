from django.shortcuts import render
from django.http import HttpResponse

pages = {
    'runs': 'List Runs',
    'add_run': 'Add Run',
    'run_stats': 'Running Statistics'
}

# Create your views here.
def runs_view(request, topic):
    return HttpResponse(pages[topic])
