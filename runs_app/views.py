from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse

# Create your views here.
def list_runs(request):

    all_runs = models.Run.objects.all()
    context = {'runs':all_runs}

    return render(request, 'runs_app/runs.html', context=context)

def run_detail(request):

    my_var = {'first_name': 'first', 'last_name': 'last',
        'some_list': [1,2,3], 'user_logged_in': True
    }
    return render(request, 'runs_app/run.html', context = my_var)

