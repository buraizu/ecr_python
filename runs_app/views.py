from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse

# Create your views here.
def runs_view(request):
    return render(request, 'runs_app/example.html')

