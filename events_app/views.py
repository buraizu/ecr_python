from django.shortcuts import render
from django.views.generic import ListView
from events_app.models import Event

# Create your views here.
class EventListView(ListView):
    model = Event
    context_object_name = "event_list"