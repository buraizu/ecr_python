from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse

# Create your views here.
def runs_view(request):
    return render(request, 'runs_app/example.html')

def run_view(request):

    my_var = {'first_name': 'first', 'last_name': 'last',
        'some_list': [1,2,3], 'user_logged_in': True
    }
    return render(request, 'runs_app/run.html', context = my_var)

